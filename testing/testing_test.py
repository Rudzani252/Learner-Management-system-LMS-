import pytest
from Singleton import AppConfig
from SupportTicket import SupportTicketFactory
from Assessments import Assessment

def test_singleton_same_instance():

    config1 = AppConfig()
    config2 = AppConfig()

    assert config1 is config2

def test_create_technical_ticket():

    ticket = SupportTicketFactory.create_ticket(
        learner_id=1,
        learner_email="test@gmail.com",
        ticket_type="technical",
        description="Cannot login",
        status="Open")
    assert ticket.ticket_type == "Technical"
    assert ticket.ticket_description == "Cannot login"
    assert ticket.status == "Open"

def test_percentage_calculation():

    strategy = Assessment.PercentageStrategy()

    result = strategy.calculate_percentage(
        35,
        50
    )

    assert result == 70


def test_pass_result():

    strategy = Assessment.PassFailStrategy()

    result = strategy.check_pass_or_fail(
        35,
        50
    )

    assert result == "Pass"


def test_fail_result():

    strategy = Assessment.PassFailStrategy()

    result = strategy.check_pass_or_fail(
        20,
        50
    )

    assert result == "Fail"


def test_invalid_ticket_type():

    with pytest.raises(ValueError):

        SupportTicketFactory.create_ticket(
            learner_id=1,
            learner_email="test@gmail.com",
            ticket_type="invalid",
            description="Test ticket",
            status="Open"
        )