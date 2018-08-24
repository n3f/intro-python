def make_car(manufacturer, model, **kwargs):
    car = dict(manufacturer=manufacturer, model=model)
    car.update(kwargs)
    return car