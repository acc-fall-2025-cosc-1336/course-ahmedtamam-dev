def add_inventory(widgets: dict, widget_name: str, quantity: int):
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity


def remove_inventory_widget(widgets: dict, widget_name: str):
    if widget_name in widgets:
        del widgets[widget_name]
        return 'Record deleted'
    return 'Item not found'