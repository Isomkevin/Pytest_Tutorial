import pytest
from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock

@pytest.fixture
def cart():
  # All Cart Details defined here
  return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
  cart.add('Apple')
  assert cart.size() == 1


def test_when_item_added_the_cart_contains_item(cart):
  cart.add('Apple')
  assert 'Apple' in cart.get_items()


def test_when_add_more_than_max_size_should_fail(cart):
  for _ in range(5):
    cart.add('Apple')
  with pytest.raises(OverflowError):
    cart.add('Apple')


def test_can_get_total_prize(cart):
  cart.add('Apple')
  cart.add('Orange')
  item_database = ItemDatabase()

  def mock_get_item(item: str):
    if item ==  'Apple':
      return 3.0
    if item == 'Orange':
      return 2.0
  
  item_database.get = Mock(side_effect=mock_get_item)
  assert cart.get_total_prize(item_database) == 5.0