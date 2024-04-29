from du10_graph_traversal import *

def reachable_size_test():
    #pro počáteční vrchol A bude výsledkem dvojice (6, 6)
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")
    a.succs = [d]
    b.succs = [e, a]
    c.succs = [e, f, g]
    d.succs = [b]
    e.succs = [g, f]
    draw_example()
    assert reachable_size(a) == (6, 6)

    #pro počáteční vrchol C bude výsledkem dvojice (4, 5)
    clear_flags([a, b, c, d, e, f, g])
    assert reachable_size(c) == (4, 5)

    #pro počáteční vrchol E bude výsledkem dvojice (3, 2)
    clear_flags([a, b, c, d, e, f, g])
    assert reachable_size(e) == (3, 2)

    x = Vertex("X")
    assert reachable_size(x) == (1, 0)


def has_cycle_test():
    #pro počáteční vrchol A bude výsledkem ‹True›
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")
    a.succs = [d]
    b.succs = [e, a]
    c.succs = [e, f, g]
    d.succs = [b]
    e.succs = [g, f]
    draw_graph({a, b, c, d, e, f, g}, "what.dot")
    assert has_cycle(a)

    #pro počáteční vrchol C bude výsledkem ‹False›
    clear_flags([a, b, c, d, e, f, g])
    assert not has_cycle(c)

    #pro počáteční vrchol E bude výsledkem ‹False›
    clear_flags([a, b, c, d, e, f, g])
    assert not has_cycle(e)

    x = Vertex("X")
    assert not has_cycle(x)

    a = Vertex("A")
    b = Vertex("B")
    a.succs = [b]
    b.succs = [b]
    assert has_cycle(a)

    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    a.succs = [b]
    b.succs = [c]
    c.succs = [b]
    assert has_cycle(a)

    a = Vertex("A")
    a.succs = [a]
    assert has_cycle(a)

    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")
    a.succs = [b]
    b.succs = [c]
    c.succs = [d]
    d.succs = [e]
    e.succs = [f]
    f.succs = [g]
    g.succs = [a]
    draw_graph([a, b, c, d, e, f, g], "moj.dot")
    assert has_cycle(e)

    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    a.succs = [b, c]
    b.succs = []
    c.succs = [b]
    draw_graph([a, b, c], "idkuzfakt.dot")
    assert not has_cycle(a)

    s = Vertex("s")
    q = Vertex("q")
    t = Vertex("t")
    y = Vertex("y")
    r = Vertex("r")
    v = Vertex("v")
    w = Vertex("w")
    x = Vertex("x")
    z = Vertex("z")
    u = Vertex("u")
    o = Vertex("o")
    n = Vertex("n")

    s.succs = [v]
    q.succs = [s, w, t]
    t.succs = [w, x, y]
    y.succs = [q]
    r.succs = [y, u, o]
    v.succs = [w]
    w.succs = [s, ]
    x.succs = [w, z]
    z.succs = [x]
    u.succs = [y]
    o.succs = [n]

    draw_graph([s, q, t, y, r, v, w, x, z, u, o, n], "cviko.dot")
    assert has_cycle(q)

    clear_flags([s, q, t, y, r, v, w, x, z, u, o, n])
    assert has_cycle(r)

    clear_flags([s, q, t, y, r, v, w, x, z, u, o, n])
    assert has_cycle(z)

    clear_flags([s, q, t, y, r, v, w, x, z, u, o, n])
    assert not has_cycle(o)

    clear_flags([s, q, t, y, r, v, w, x, z, u, o, n])
    assert not has_cycle(n)
    


def is_tree_test():
    #pro počáteční vrchol A bude výsledkem ‹False›
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")
    a.succs = [d]
    b.succs = [e, a]
    c.succs = [e, f, g]
    d.succs = [b]
    e.succs = [g, f]
    assert not is_tree(a)

    #pro počáteční vrchol C bude výsledkem ‹False›
    clear_flags([a, b, c, d, e, f, g])
    assert not is_tree(c)

    #pro počáteční vrchol E bude výsledkem ‹True›
    clear_flags([a, b, c, d, e, f, g])
    assert is_tree(e)

    x = Vertex("X")
    assert is_tree(x)


def distance_test():
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")
    a.succs = [d]
    b.succs = [e, a]
    c.succs = [e, f, g]
    d.succs = [b]
    e.succs = [g, f]
    assert distance(a, g) == 4

    clear_flags([a, b, c, d, e, f, g])
    assert distance(c, g) == 1

    clear_flags([a, b, c, d, e, f, g])
    assert distance(e, d) is None

    x = Vertex("X")
    assert distance(x, a) is None

    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    a.succs = [c, b]
    b.succs = [e]
    c.succs = [d]
    d.succs = [e]
    assert distance(a, e) == 2

def clear_flags(vertecies: list[Vertex]):
    for v in vertecies:
        v.flag = None


reachable_size_test()
has_cycle_test()
is_tree_test()
distance_test()
