import pytest
from assertpy import assert_that

from core.app.api.api_client import API
from core.models.model_company import CompanyDC


@pytest.mark.case("BG-11111")
@pytest.mark.parametrize("company_data", [CompanyDC(name="aqa-company", location="Seoul")])
def test_company(api: API, company_data: CompanyDC):
    company = api.company.get_company(company_data)

    assert_that(company.name).is_equal_to(company_data.name)
    assert_that(company.location).is_equal_to(company_data.location)
