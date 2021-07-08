Title: Singular Value Decomposition - developing a visual intuition
Date: 2021-07-01 16:04
Modified: 2021-07-01 16:04
Slug: svd
PageType: ProjectDescription

**This post is in progress..**

* [Properties of orthogonal matrices](https://medium.com/jun-devpblog/linear-algebra-9-properties-of-orthogonal-matrices-840b1d28ac20)
* [history of SVD](https://conservancy.umn.edu/bitstream/handle/11299/1868/952.pdf?sequence=1&isAllowed=y)

For the longest time, I could not figure out what the Singular Value Decomposition (SVD) of a matrix meant. 
Sure, its a way to break up a matrix into a product of three different matrices; but the potential of linear algebra is largely wasted if one doesn't develop a visual understanding of what is happening.
So, what is happening with the SVD visually?
To understand this, it is important to know what a matrix is doing, visually.
The **best** resource to understand this is to watch [3Blue1Brown's series](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) on linear algebra.
I'll give a quick summary here, but if you really want to understand this stuff, you really should watch those videos.

In essence, every matrix is a mapping of points to other points.
We can represent points in abstract spaces by vectors -- so a matrix can be thought of as a mapping from vectors to other vectors.
This mapping, or *transformation* is applied through an operation called matrix multiplication, i.e., multiplying the matrix with the vector representation of the point (or simply the vector from now on).
For example, the point $[1 \; 0]^T$ is *transformed* (or *mapped*) to the point $[2 \; 0]^T$ using the following matrix multiplication

<< change this example to something that rotates and stretches >>

$$ \begin{bmatrix}
	2 & 0\\
	0 & 2
   \end {bmatrix} \begin{bmatrix}
			1\\
			0
	          \end{bmatrix} = \begin{bmatrix}
					2\\
					0
				  \end{bmatrix} $$


Once you can start seeing matrices as transformations of a (appropriate dimensional) space, we can start to build our intuition on top of that.
The eigenvectors of a matrix give us the directions which are unaffected by the rotation caused by the matrix's transformation. 
The corresponding eigenvalues give us the scaling factor for that given direction.
In the same way, the singular values and singular vectors give us the direction and multiplier of the direction of biggest increase when the matrix transformation is applied.
