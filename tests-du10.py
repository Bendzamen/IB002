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
    assert reachable_size(c) == (4, 5)

    #pro počáteční vrchol E bude výsledkem dvojice (3, 2)
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
    assert has_cycle(a)

    #pro počáteční vrchol C bude výsledkem ‹False›
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
    assert not has_cycle(c)

    #pro počáteční vrchol E bude výsledkem ‹False›
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

    """
    vrchol ‹a› má následníky: ‹b›, ‹c›
    vrchol ‹b› nemá žádné následníky
    vrchol ‹c› má následníky: ‹b›
    Test volání: has_cycle(a) Špatný výsledek True, měl být False.
    """

    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    a.succs = [b, c]
    b.succs = []
    c.succs = [b]
    draw_graph([a, b, c], "idkuzfakt.dot")
    assert not has_cycle(a)


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
    assert not is_tree(c)

    #pro počáteční vrchol E bude výsledkem ‹True›
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
    assert distance(c, g) == 1

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


reachable_size_test()
has_cycle_test()
is_tree_test()
distance_test()
