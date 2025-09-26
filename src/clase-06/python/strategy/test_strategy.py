from python.strategy.strategy import Navigator, CarRoute, WalkRoute, PublicTransportRoute

def test_strategy_switch():
    nav = Navigator(CarRoute())
    r1 = nav.build_route("A", "B")
    assert "auto" in r1

    nav.set_strategy(WalkRoute())
    r2 = nav.build_route("A", "B")
    assert "pie" in r2

    nav.set_strategy(PublicTransportRoute())
    r3 = nav.build_route("A", "B")
    assert "transporte público" in r3
