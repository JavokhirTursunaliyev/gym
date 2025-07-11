function addToCart(productId) {
  alert("Product " + productId + " added to cart!");
  // TODO: Connect to backend/cart logic
}

function toggleFavorite(productId, element) {
  element.classList.toggle('favorited');
  // TODO: Send favorite status to backend if needed
}
