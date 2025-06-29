#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import threading
import os
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Allow recursion depth ≥ 64
sys.setrecursionlimit(10000)

# All 8 knight moves
MOVES = [(2,1),(1,2),(-1,2),(-2,1),
         (-2,-1),(-1,-2),(1,-2),(2,-1)]


class KnightTourApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Knight's Tour")
        self._create_menu()
        self._load_start_screen()

    def _create_menu(self):
        menubar = tk.Menu(self.master)
        gm = tk.Menu(menubar, tearoff=0)
        gm.add_command(label="New Game", command=self._restart)
        gm.add_separator()
        gm.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="Game", menu=gm)
        self.master.config(menu=menubar)

    def _load_start_screen(self):
        """Start screen: background + size entry + START."""
        base = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(base, "start_bg.png")
        try:
            bg = Image.open(img_path)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot load {img_path}:\n{e}")
            self.master.destroy()
            return

        w, h = bg.size
        self.master.geometry(f"{w}x{h}")
        try:
            res = Image.Resampling.LANCZOS
        except AttributeError:
            res = Image.LANCZOS
        bg = bg.resize((w, h), res)
        self.bg_photo = ImageTk.PhotoImage(bg)

        # full‐screen canvas + dimming overlay
        self.start_frame = tk.Frame(self.master)
        self.start_frame.pack(fill="both", expand=True)
        canvas = tk.Canvas(self.start_frame, width=w, height=h, highlightthickness=0)
        canvas.pack()
        canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
        canvas.create_rectangle(0, 0, w, h, fill="black", stipple="gray50", outline="")

        # central control panel
        panel = tk.Frame(canvas, bg="#222")
        canvas.create_window(w/2, h*0.7, window=panel)

        # Board size
        tk.Label(panel, text="Board size (5–20):",
                 fg="white", bg="#222", font=("Arial", 14)
        ).grid(row=0, column=0, padx=8, pady=8, sticky="e")
        self.size_var = tk.StringVar(master=self.master, value="8")
        tk.Entry(panel, textvariable=self.size_var,
                 font=("Arial", 14), width=4, justify="center"
        ).grid(row=0, column=1, padx=8, pady=8, sticky="w")

        # START button
        tk.Button(panel, text="START",
                  font=("Arial", 16, "bold"), bg="#4CAF50", fg="white",
                  padx=20, pady=6, command=self._on_start
        ).grid(row=1, column=0, columnspan=2, pady=(0,12))

    def _on_start(self):
        """Validate n and switch to game screen."""
        try:
            n = int(self.size_var.get())
            if not (5 <= n <= 20):
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Enter an integer 5–20.")
            return
        self.n = n
        self.start_frame.destroy()
        self._init_game()

    def _init_game(self):
        """Set up board canvas + control panel."""
        self.cell_size = 60
        board_px = self.cell_size * self.n
        # allow extra width for panel
        self.master.geometry(f"{board_px+240}x{board_px+20}")

        # store game frame so we can destroy it later
        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack(fill="both", expand=True)
        container = self.game_frame

        # --- Board canvas ---
        self.canvas = tk.Canvas(container, width=board_px, height=board_px)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.board = [[0]*self.n for _ in range(self.n)]
        self.running = False
        self._draw_board()
        self.canvas.bind("<Button-1>", self._on_board_click)

        # --- Control panel ---
        ctrl = tk.Frame(container)
        ctrl.grid(row=0, column=1, sticky="n", padx=10, pady=10)

        # Speed slider
        tk.Label(ctrl, text="Animation speed (ms):").pack(pady=(0,6))
        self.speed_var = tk.IntVar(value=180)
        tk.Scale(ctrl, from_=50, to=500, orient="horizontal",
                 variable=self.speed_var, length=180).pack()

        # Pause/Resume
        self.paused = False
        self.pause_btn = tk.Button(ctrl, text="Pause",
                                   command=self._toggle_pause)
        self.pause_btn.pack(fill="x", pady=8)

        # Move counter
        self.move_var = tk.StringVar(value=f"Move: 0/{self.n*self.n}")
        tk.Label(ctrl, textvariable=self.move_var).pack(pady=6)

        # Timer
        self.time_var = tk.StringVar(value="Time: 0s")
        tk.Label(ctrl, textvariable=self.time_var).pack(pady=6)

    def _draw_board(self):
        s = self.cell_size
        for r in range(self.n):
            for c in range(self.n):
                x0, y0 = c*s, r*s
                x1, y1 = x0+s, y0+s
                color = "#EEE" if (r+c)%2 else "#FFF"
                self.canvas.create_rectangle(x0, y0, x1, y1,
                                             fill=color, outline="black")

    def _on_board_click(self, ev):
        if self.running:
            return
        c, r = ev.x // self.cell_size, ev.y // self.cell_size
        if not (0 <= r < self.n and 0 <= c < self.n):
            return
        # reset board & redraw
        self.canvas.delete("all")
        self._draw_board()
        self.board = [[0]*self.n for _ in range(self.n)]
        self.running = True
        # start timer
        self.start_time = time.time()
        self._update_timer()
        # solve in background
        threading.Thread(target=self._run_tour, args=(r, c), daemon=True).start()

    def _update_timer(self):
        if not self.running:
            return
        elapsed = int(time.time() - self.start_time)
        self.time_var.set(f"Time: {elapsed}s")
        self.master.after(1000, self._update_timer)

    def _run_tour(self, sr, sc):
        if not self._solve(sr, sc, 1):
            messagebox.showerror("Knight's Tour", "No tour from that square.")
            self.running = False
            return
        # build path
        self.path = [None] * (self.n*self.n + 1)
        for r in range(self.n):
            for c in range(self.n):
                st = self.board[r][c]
                if st > 0:
                    self.path[st] = (r, c)
        self.canvas.delete("knight")
        self._animate(1)

    def _count_moves(self, x, y):
        cnt = 0
        for dx, dy in MOVES:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.n and 0 <= ny < self.n and self.board[nx][ny] == 0:
                cnt += 1
        return cnt

    def _solve(self, x, y, step):
        self.board[x][y] = step
        if step == self.n * self.n:
            return True
        nbrs = []
        for dx, dy in MOVES:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.n and 0 <= ny < self.n and self.board[nx][ny] == 0:
                nbrs.append((self._count_moves(nx, ny), nx, ny))
        nbrs.sort(key=lambda t: t[0])
        for _, nx, ny in nbrs:
            if self._solve(nx, ny, step+1):
                return True
        self.board[x][y] = 0
        return False

    def _animate(self, k):
        """Draw step k and schedule k+1, with proper bounds-checking."""
        if k >= len(self.path):
            # end of path
            self.running = False
            return self._show_win_screen()

        if getattr(self, "paused", False):
            # if paused, retry same k shortly
            return self.master.after(100, lambda k=k: self._animate(k))

        # update move counter
        self.move_var.set(f"Move: {k}/{self.n*self.n}")

        # draw step k
        r, c = self.path[k]
        s = self.cell_size
        x, y = c*s + s//2, r*s + s//2
        self.canvas.create_text(x, y, text=str(k),
                                font=("Arial", 14, "bold"), fill="red")
        self.canvas.delete("knight")
        self.canvas.create_text(x, y, text="♞",
                                font=("Segoe UI Symbol", int(s*0.8)),
                                fill="black", tags="knight")

        # schedule next
        delay = self.speed_var.get()
        self.master.after(delay, lambda nxt=k+1: self._animate(nxt))

    def _toggle_pause(self):
        self.paused = not self.paused
        self.pause_btn.config(text="Resume" if self.paused else "Pause")

    def _show_win_screen(self):
        """Clean up and show You Win! + stats + buttons."""
        # destroy the game frame so win screen is visible
        if hasattr(self, "game_frame"):
            self.game_frame.destroy()

        win = tk.Frame(self.master, bg="#222")
        win.pack(fill="both", expand=True)
        win.lift()

        elapsed = int(time.time() - self.start_time)
        tk.Label(win, text="You Win!", font=("Arial", 48, "bold"),
                 fg="white", bg="#222").pack(pady=20)
        tk.Label(win, text=f"Moves: {self.n*self.n}", font=("Arial", 24),
                 fg="white", bg="#222").pack()
        tk.Label(win, text=f"Time: {elapsed}s", font=("Arial", 24),
                 fg="white", bg="#222").pack(pady=(0, 10))
        tk.Label(win, text="Click “Play Again” to restart or “Exit Game” to quit.",
                 font=("Segoe UI", 14), fg="white", bg="#222").pack(pady=(0, 20))

        btnf = tk.Frame(win, bg="#222")
        btnf.pack(pady=10)
        tk.Button(btnf, text="Play Again", font=("Arial", 16),
                  width=12, command=self._restart).grid(row=0, column=0, padx=10)
        tk.Button(btnf, text="Exit Game", font=("Arial", 16),
                  width=12, command=self.master.quit).grid(row=0, column=1, padx=10)

    def _restart(self):
        for w in self.master.winfo_children():
            w.destroy()
        self.__init__(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    app = KnightTourApp(root)
    root.mainloop()
