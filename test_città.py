import funzioni as f

def test_città():
    città = f.città("Roma", "Italia")
    assert città == "Roma, Italia"