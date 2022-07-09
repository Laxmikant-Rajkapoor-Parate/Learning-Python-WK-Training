def outer_fn():
    text = "Laxmikant"

    def inner_fn():
        new_text = text + " Parate"
        print(new_text)

    return inner_fn

fn = outer_fn()
fn()