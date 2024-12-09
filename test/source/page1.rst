测试页1
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _modes-of-convergence:

我们已经学习了一些收敛的概念, 它们之间的关系可以用下图总结:

.. tikz::
   :align: center
   :xscale: 100
   :libs: arrows.meta,positioning,calc,cd,arrows
   :packages: amsfonts, [slantfont,boldfont]xeCJK, pifont

   \node (uniform) at (3, 0) {$\text{({\color{cyan}近})一致收敛}$};
   \node (ae) at (-7,-3) {$\text{({\color{magenta}子列})几乎处处收敛}$};
   \node (measure) at (7, -3) {$\text{依测度收敛}$};
   \node (norm) at (-3, -7) {$\text{强收敛（依范数收敛）}$};
   \node (weak) at (-3, -9) {$\text{弱收敛}$};

   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=1em}] (uniform) -- (ae) node[midway, below] {$\checkmark$};
   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=-1em}] (ae) -- (uniform) node[sloped, anchor=center, midway, above] {{\color{red}$\boldsymbol{\times}$}, ~~ {\color{cyan} Egorov ($m E < \infty$)}};

   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={yshift=0.3em}] (ae) -- (measure) node[midway, above] {{\color{red}$\boldsymbol{\times}$}, ~~ $m E < \infty$};
   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={yshift=-0.3em}] (measure) -- (ae) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}, ~~ {\color{magenta} Riesz ($m E < \infty$)}};

   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=0.5em}] (norm) -- (ae) node[midway, above] {\color{red}$\boldsymbol{\times}$};
   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=-0.5em}] (ae) -- (norm) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}, ~ $\lVert f_n \rVert_p \to \lVert f \rVert_p$};

   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=-0.9em}] (norm) -- (measure) node[midway, above] {$\checkmark$};
   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=0.9em}] (measure) -- (norm) node[sloped, anchor=center, midway, below] {{\color{red}$\boldsymbol{\times}$}, ~~ $\text{等度绝对连续积分}$ ($m E < \infty$)};

   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=-0.3em}] (norm) -- (weak) node[midway, left] {$\checkmark$};
   \draw[arrows={-{Stealth[length=3mm, width=2mm]}}, transform canvas={xshift=0.3em}] (weak) -- (norm) node[midway, right] {\color{red}$\boldsymbol{\times}$};

上图中, :math:`A \xrightarrow{\color{red} \boldsymbol{\times}} B` 表示 :math:`A` 不蕴含 (不能推出) :math:`B`,
如果 :math:`\color{red} \times` 之后有注释, 则表示在某些条件下成立, 相应的结论也可能会弱一些 (对应括号中同颜色的文字).
:math:`A \xrightarrow{\checkmark} B` 表示 :math:`A` 蕴含 :math:`B`.

- 几乎处处收敛但不依测度收敛的例子 (注意, 这里必须有 :math:`m E = \infty`):

  .. math::

      f_n(x) = \begin{cases}
      1, & x \in [n, n + 1], \\
      0, & x \in (-\infty, n) \cup (n + 1, \infty).
      \end{cases}

  可以验证 :math:`f_n(x)` 处处收敛到 :math:`0` 但不依测度收敛到 :math:`0`.

- 依测度收敛但不几乎处处收敛的例子: :math:`E = [0, 1]`,

  .. math::
      :label: modes-of-convergence-eg-1

      f_n(x) = \chi_{\left[ \frac{i}{2^k}, \frac{i + 1}{2^k} \right]}, \quad n = 2^k + i, \quad 0 \leqslant i < 2^k.

  可以验证 :math:`f_n(x)` 依测度收敛到 :math:`0` 但不几乎处处 (实际上是, 处处都不) 收敛到 :math:`0`.

- 强收敛但不几乎处处收敛的例子: :eq:`modes-of-convergence-eg-1` 中的函数序列也在 :math:`L^1(E)` 中的强收敛到 :math:`0`.

- 依测度收敛但不强收敛的例子: 只要对 :eq:`modes-of-convergence-eg-1` 中的函数序列稍作修改即可:

  .. math::

      f_n(x) = 2^k \chi_{\left[ \frac{i}{2^k}, \frac{i + 1}{2^k} \right]}, \quad n = 2^k + i, \quad 0 \leqslant i < 2^k.

  可以验证 :math:`f_n(x)` 依测度收敛到 :math:`0` 但不强收敛到 :math:`0`.
