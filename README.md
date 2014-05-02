FunctionViewer
==============

As a programming exercise, we are building a function viewer.

The basic idea is that we have a view of some function of x and y -- f(x,y) that produces a value V = f(x,y).

The value V is translated into a color C. 

An example of this kind of thing includes views of the Mandelbrot set.

The viewer can be thought of as a function on the (x',y') points in the view pane -- C = p(x',y').

We can zoom and pan the view pane. There is a UI "controller" on the view.

That means that there is a controllable 2-way mapping M between the f(x,y) points and the view pane p(x',y') points.

A typical mapping might be linear so that x' = x0 + xt * x  and y' = y0 + yt * y. 

(I am assuming that xt and yt are tangents calculated from a "camera" window to eyeball. 
But they can be quite arbitrary scale factors depending on our viewing ideas.
Also, the mapping does not have to be linear. It could be logrithmic or some other transform.)

The view pane also places limits on the (x',y') where x' is limited to [xa',xb'] and y' is limited to [ya', yb'].

We can also use the idea that the view pane contains discrete pixels to limit the number of f(x,y) values that we need to compute. The discrete pixels define a finite set of (x',y'). Our 2-way mapping can map that set to a set of (x,y) input values. We might also have a display strategy where we start out with fat pixels and then refine the display to finer pixels. That means that we have some controllable iterator that produces a series of  (x,y) points within the limits defined by the view pane and the mapping M.
 
