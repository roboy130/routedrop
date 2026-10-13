
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="RouteDrop API",
    description="Delivery recommendations optimized around a driver's destination.",
    version="0.1.0",
)


class DeliveryOffer(BaseModel):
    id: int
    pickup: str
    dropoff: str
    payout: float = Field(gt=0)
    delivery_miles: float = Field(gt=0)
    delivery_minutes: int = Field(gt=0)
    detour_minutes: int = Field(ge=0)


class RecommendationRequest(BaseModel):
    destination: str
    max_delivery_miles: float = Field(default=10, gt=0)
    offers: list[DeliveryOffer]


class RankedOffer(BaseModel):
    id: int
    pickup: str
    dropoff: str
    payout: float
    delivery_miles: float
    detour_minutes: int
    estimated_total_minutes: int
    estimated_hourly_rate: float
    score: float


@app.get("/")
def home():
    return {
        "message": "Welcome to RouteDrop!",
        "status": "running",
    }


@app.get("/offers")
def get_sample_offers():
    """Return fictional delivery offers for testing."""
    return [
        {
            "id": 1,
            "pickup": "Bel Air",
            "dropoff": "Abingdon",
            "payout": 9.50,
            "delivery_miles": 4.0,
            "delivery_minutes": 18,
            "detour_minutes": 4,
        },
        {
            "id": 2,
            "pickup": "Edgewood",
            "dropoff": "Bel Air",
            "payout": 14.00,
            "delivery_miles": 8.0,
            "delivery_minutes": 30,
            "detour_minutes": 15,
        },
        {
            "id": 3,
            "pickup": "Aberdeen",
            "dropoff": "Edgewood",
            "payout": 7.00,
            "delivery_miles": 3.0,
            "delivery_minutes": 15,
            "detour_minutes": 1,
        },
    ]


@app.post("/recommendations", response_model=list[RankedOffer])
def recommend_deliveries(request: RecommendationRequest):
    """Rank offers by estimated earnings per total minute."""
    recommendations = []

    for offer in request.offers:
        # Enforce the driver's maximum delivery distance.
        if offer.delivery_miles > request.max_delivery_miles:
            continue

        total_minutes = offer.delivery_minutes + offer.detour_minutes

        # Account for delivery time AND the extra time caused by the detour.
        hourly_rate = offer.payout / total_minutes * 60

        recommendations.append(
            RankedOffer(
                id=offer.id,
                pickup=offer.pickup,
                dropoff=offer.dropoff,
                payout=offer.payout,
                delivery_miles=offer.delivery_miles,
                detour_minutes=offer.detour_minutes,
                estimated_total_minutes=total_minutes,
                estimated_hourly_rate=round(hourly_rate, 2),
                score=round(hourly_rate, 2),
            )
        )

    # Highest estimated earnings per hour first.
    recommendations.sort(key=lambda offer: offer.score, reverse=True)

    return recommendations