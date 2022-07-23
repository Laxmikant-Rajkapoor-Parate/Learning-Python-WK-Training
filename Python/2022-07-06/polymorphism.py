class bank:
    def __init__(self, roi) -> None:
        self.roi = roi

    def get_roi(self):
        return self.roi

#inherited class
class SBI(bank):
    def __init__(self, roi) -> None:
        super().__init__(roi)

#inherited class
class HDFC(bank):
    def __init__(self, roi) -> None:
        super().__init__(roi)

sbi = SBI(5)
hdfc = HDFC(6)

print(f'ROI SBI: {sbi.get_roi()}')
print(f'ROI HDFC: {hdfc.get_roi()}')