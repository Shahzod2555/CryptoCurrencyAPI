from fastapi import APIRouter
from .init import cmc_client

router = APIRouter(
	prefix='/cryptocurrencies'
)

@router.get('')
async def get_cryptocurrencies():
	data = await cmc_client.get_listings()
	result = []
	for crypto in data:
		result.append({
			"name": crypto.get("name"),
			"slug": crypto.get("slug"),
			"date_added": crypto.get("date_added"),
			"circulating_supply": crypto.get("circulating_supply"),
			"total_supply": crypto.get("total_supply"),
			"is_active": crypto.get("is_active"),
			"price_usd": crypto.get("quote", {}).get("USD", {}).get("price"),
			"percent_change_7d": crypto.get("quote", {}).get("USD", {}).get("percent_change_7d"),
			"volume_24h": crypto.get("quote", {}).get("USD", {}).get("volume_24h")
		})
	return result


@router.get('/{currency_id}')
async def get_cryptocurrency(currency_id: int):
	data = await cmc_client.get_currency(currency_id)
	result = {
		"name": data.get("name"),
		"slug": data.get("slug"),
		"date_added": data.get("date_added"),
		"circulating_supply": data.get("circulating_supply"),
		"total_supply": data.get("total_supply"),
		"is_active": data.get("is_active"),
		"price_usd": data.get("quote", {}).get("USD", {}).get("price"),
		"percent_change_7d": data.get("quote", {}).get("USD", {}).get("percent_change_7d"),
		"volume_24h": data.get("quote", {}).get("USD", {}).get("volume_24h")
	}
	return result
