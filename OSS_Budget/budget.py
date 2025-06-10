import datetime
from expense import Expense
import csv

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def save_to_csv(self, filename="expenses.csv"):
        if not self.expenses:
            print("저장할 지출 내역이 없습니다.\n")
            return
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["날짜", "카    테고리", "설명", "금액"])
            for e in self.expenses:
                writer.writerow([e.date, e.category, e.description, e.amount])
        print(f"{filename} 파일로 저장 완료.\n")
    
    def total_by_category(self):
    if not self.expenses:
        print("지출 내역이 없습니다.\n")
        return

    category_totals = {}
    for e in self.expenses:
        if e.category in category_totals:
            category_totals[e.category] += e.amount
        else:
            category_totals[e.category] = e.amount

    print("\n[카테고리별 지출 합계]")
    for category, total in category_totals.items():
        print(f"{category}: {total}원")
    print()

    def delete_expense(self, index):
    if not self.expenses:
        print("지출 내역이 없습니다.\n")
        return

    if 0 < index <= len(self.expenses):
        removed = self.expenses.pop(index - 1)
        print(f"{index}번 지출 항목이 삭제되었습니다: {removed}\n")
    else:
        print("잘못된 번호입니다.\n")

   



