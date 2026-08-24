import unittest

# ==========================================
# 1. FUNCTIONS TO TEST (Supply Chain Logic)
# ==========================================

def calculate_ontime_rate(total_deliveries, ontime_deliveries):
    """Calculates the percentage of on-time deliveries."""
    if total_deliveries <= 0:
        return 0.0
    # Input validation: on-time deliveries cannot exceed total deliveries
    if ontime_deliveries > total_deliveries:
        return 100.0
    return round((ontime_deliveries / total_deliveries) * 100, 2)


def categorize_lead_time(days):
    """Categorizes shipping lead times into speed zones."""
    if days < 0:
        return "Invalid"
    if days <= 3:
        return "Fast"
    elif days <= 7:
        return "Standard"
    else:
        return "Delayed"


# ==========================================
# 2. AUTOMATED UNIT TESTS
# ==========================================
class TestSupplyChainCalculations(unittest.TestCase):

    # --- Tests for On-Time Delivery Rate ---
    def test_ontime_rate_normal(self):
        # 10 deliveries, 8 on time = should be exactly 80.0%
        self.assertEqual(calculate_ontime_rate(10, 8), 80.0)

    def test_ontime_rate_zero_deliveries(self):
        # 0 deliveries should safely return 0.0 instead of crashing (division by zero)
        self.assertEqual(calculate_ontime_rate(0, 5), 0.0)

    def test_ontime_rate_perfect(self):
        # All deliveries on time = should be exactly 100.0%
        self.assertEqual(calculate_ontime_rate(5, 5), 100.0)

    # --- Tests for Lead Time Categorization ---
    def test_lead_time_fast(self):
        # 2 days should be categorized as "Fast"
        self.assertEqual(categorize_lead_time(2), "Fast")

    def test_lead_time_standard(self):
        # 5 days should be categorized as "Standard"
        self.assertEqual(categorize_lead_time(5), "Standard")

    def test_lead_time_delayed(self):
        # 10 days should be categorized as "Delayed"
        self.assertEqual(categorize_lead_time(10), "Delayed")

    def test_lead_time_negative(self):
        # Negative days should be categorized as "Invalid"
        self.assertEqual(categorize_lead_time(-3), "Invalid")


# ==========================================
# 3. RUN TESTS
# ==========================================
if __name__ == '__main__':
    print("--- RUNNING AUTOMATED TESTS ---")
    unittest.main()