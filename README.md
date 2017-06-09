
Generate Euler-Spirals (Clothoids)
==================================

Calculate the points on an euler spiral using the length and bounding curvatures.


## Usage

```
from eulerspiral import eulerspiral

spiral = eulerspiral.EulerSpiral.createFromLengthAndCurvature(length, curvStart, curvEnd)
(x, y, t) = spiral.calc(s, x0, y0, curvStart, hdg)
```

## Reference

Kimia, B. B., Frankel, I., & Popescu, A. M. (2003). Euler spiral for shape completion. International journal of computer vision, 54(1), 159-182.
