from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

from django import template

from task.models import *
from task.models import MenuItem

register = template.Library()


@dataclass
class TreeNode:
    name: str
    absolute_url: str
    tag: MenuItem
    children: Optional[list] = None


def get_ancestors(query_set, item_id):
    ancestors = [item_id]
    for item in query_set:
        if item.id == item_id:
            current_item = item
            while current_item and current_item.parent_id:
                parent_id = current_item.parent_id
                parent_item = [item for item in query_set if item.id == parent_id][0]
                ancestors.append(parent_item.id)
                current_item = parent_item

    return ancestors


def build_menu_tree(nodes, node_children, branch_path):
    tree = []
    for node in nodes:
        if node.id in branch_path:
            tree.append(
                TreeNode(
                    node.name,
                    node.get_absolute_url(),
                    node,
                    build_menu_tree(node_children[node.id], node_children, branch_path),
                )
            )
        else:
            tree.append(TreeNode(node.name, node.get_absolute_url(), node))
    return tree


@register.inclusion_tag("task/menu.html")
def draw_menu(menu_name, cat_selected=0):
    flat_menu = MenuItem.objects.filter(menu__name__contains=menu_name)

    node_children = defaultdict(list)
    roots = []
    for tag in flat_menu:
        if tag.parent_id:
            node_children[tag.parent_id].append(tag)
        else:
            roots.append(tag)

    expand_branch_path = get_ancestors(flat_menu, cat_selected)

    menu_tree = build_menu_tree(roots, node_children, expand_branch_path)

    return {"menu": menu_tree, "cat_selected": cat_selected}
