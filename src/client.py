from aiohttp import ClientSession


class CMCHTTPClient:
	def __init__(self, base_url: str, api_key: str):
		self.base_url = base_url
		self.api_key = api_key
		self._session = None

	async def get_listings(self):
		async with ClientSession(
			base_url=self.base_url,
			headers={'X-CMC_PRO_API_KEY': self.api_key}
		) as session:
			async with session.get("/v1/cryptocurrency/listings/latest") as resp:
				result = await resp.json()
				return result['data']

	async def get_currency(self, currency_id: int):
		async with ClientSession(
			base_url=self.base_url,
			headers={'X-CMC_PRO_API_KEY': self.api_key}
		) as session:
			async with session.get("/v2/cryptocurrency/quotes/latest", params={"id": currency_id}) as resp:
				result = await resp.json()
				return result['data'][str(currency_id)]
