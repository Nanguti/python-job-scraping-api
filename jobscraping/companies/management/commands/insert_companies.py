from typing import Any
from django.core.management.base import BaseCommand

from companies.models import Company

class Command(BaseCommand):
    help = 'Inserts predefined companies into the database'

    def handle(self, *args: Any, **options: Any):
        companies = [
            "Safaricom",
            "Equity Bank Kenya",
            "KCB",
            "Co-operative Bank of Kenya",
            "Standard Chartered",
            "Barclays Bank",
            "Britam Holdings",
            "East African Breweries",
            "Coca Cola",
            "British American Tobacco",
            "Nation Media Group",
            "Bamburi Cement",
            "Total Energies",
            "Airtel",
            "Kenya Pipeline Company",
            "Adept Technologies Ltd",
            "Kenya Airways",
            "Kenya Revenue Authority",
            "Google",
            "United Nations",
            "Deloitte",
            "KPMG",
            "PricewaterhouseCoopers LLP"
        ]

        for company_name in companies:
            Company.objects.get_or_create(name=company_name)

        self.stdout.write(self.style.SUCCESS('Successfully inserted companies'))
