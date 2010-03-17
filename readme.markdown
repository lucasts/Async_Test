Async IO - Servers Benchmark
============================

Goal
----
Just do some dumb benchmarks against non-blocking i/o web server implementations 

Sorry
-----

I'm not the best with python and shell script, please if can make some of scripts better, fork me and request pull ;-)


Requirements
------------

* bash(Linux, Mac and BSDs should had pre-installed)
* ruby 1.8.7(1.9.1 works??) (for thin) - www.ruby-lang.org
* python (for tornado and twisted) - www.python.org
* apache ( if you want to compare normal apache versus async/evented implementations) - httpd.apache.org

Optionals
--------

* matplotlib to generate graphs - http://matplotlib.sourceforge.net/index.html


Running
-------

1. open a terminal
1. clone the repository
1. go to bench dir created by git clone(a.k.a: cd Async_Test)
1. verify if requeriments and optionals are installed
1. run the benchmark script
  1.  # ./run 2000 200
  1. where 2000 is number of requests and 200 is concurrency level
1. after 2 minutes(depending on your computer) it will finish with a graph(if matplotlib ok).
1. if doesn't have matplotlib installed, just run `cat summary.txt`


