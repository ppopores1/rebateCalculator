from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# CLASS: ObtainInput
class ObtainInput:
    def __init__(self, form_data):
        self.cost_for_price = float(form_data.get('cost_for_price', 0) or 0)
        self.sale_price = float(form_data.get('sale_price', 0) or 0)
        self.guidance_margin = float(form_data.get('guidance_margin', 0) or 0)
        self.desired_margin = float(form_data.get('desired_margin', 0) or 0)
        self.rebate_percentage = float(form_data.get('rebate_percentage', 0) or 0) / 100
        self.sale_price_two = float(form_data.get('sale_price_two', 0) or 0)
        self.calculation_type = form_data.get('calculation_type', '')

        # Handle derived fields
        if self.calculation_type == 'c4' and self.desired_margin and self.cost_for_price:
            self.sale_price = self.cost_for_price + self.desired_margin
        elif self.calculation_type == 'street_smart' and self.sale_price and self.guidance_margin:
            self.cost_for_price = self.sale_price - self.guidance_margin

# METHOD: ProcessInput
class ProcessInput:
    def __init__(self, input_data):
        self.cost_for_price = input_data.cost_for_price
        self.sale_price = input_data.sale_price
        self.rebate_percentage = input_data.rebate_percentage
        self.sale_price_two = input_data.sale_price_two

    def calculate(self):
        # Basic calculations
        rebate_total = self.sale_price * self.rebate_percentage
        actual_selling_price = self.sale_price - rebate_total
        actual_margin = actual_selling_price - self.cost_for_price

        # Margin percentages
        margin_percent_before_rebate = ((self.sale_price - self.cost_for_price) / self.sale_price) * 100 if self.sale_price else 0
        margin_percent_after_rebate = (actual_margin / actual_selling_price) * 100 if actual_selling_price else 0

        # Margin impact calculations (optional field)
        margin_impact_doll = None
        margin_impact_perc = None
        if self.sale_price_two:
            adjusted_margin = self.sale_price_two - rebate_total - self.cost_for_price
            margin_impact_doll = adjusted_margin - actual_margin
            margin_impact_perc = ((adjusted_margin - actual_margin) / actual_margin) * 100 if actual_margin else 0

        # Price adjustment recommendations
        price_adjustments = None
        if actual_selling_price and actual_selling_price < self.cost_for_price * 1.05:
            price_adjustments = [
                {'label': '5% Above Cost', 'value': round(self.cost_for_price * 1.0501, 2)},
                {'label': '7% Above Cost', 'value': round(self.cost_for_price * 1.07, 2)},
                {'label': '12% Above Cost', 'value': round(self.cost_for_price * 1.12, 2)},
            ]

        # Return all calculated values
        return {
            'rebate_total': round(rebate_total, 2),
            'actual_margin': round(actual_margin, 2),
            'actual_selling_price': round(actual_selling_price, 2),
            'margin_percent_before_rebate': round(margin_percent_before_rebate, 2),
            'margin_percent_after_rebate': round(margin_percent_after_rebate, 2),
            'margin_impact_doll': round(margin_impact_doll, 2) if margin_impact_doll else None,
            'margin_impact_perc': round(margin_impact_perc, 2) if margin_impact_perc else None,
            'price_adjustments': price_adjustments
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_data = ObtainInput(request.json)
    processor = ProcessInput(input_data)
    results = processor.calculate()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
