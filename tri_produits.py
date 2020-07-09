








class TriProduits:
	"""docstring for TriProduits"""
	def __init__(self):

		self.produits_trie = []

	def tri_prod(self, produits_nontrie):

		for produit_nontrie in produits_nontrie:
			if produit_nontrie['nutriscore'] != '' :
				self.produits_trie.append( produit_nontrie )

		












