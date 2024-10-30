import tkinter as tk
from tkinter import ttk

class KioskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("키오스크 프로그램")
        self.root.geometry("800x600")
        
        # 메뉴 데이터
        self.menu_items = {
            "음료": {
                "아메리카노": 3000,
                "카페라떼": 3500,
                "카푸치노": 3500
            },
            "디저트": {
                "치즈케이크": 5000,
                "초코케이크": 5000,
                "크로플": 4000
            }
        }
        
        # 장바구니
        self.cart = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # 메인 프레임
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 메뉴 표시 영역
        self.menu_frame = ttk.LabelFrame(self.main_frame, text="메뉴", padding="10")
        self.menu_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 장바구니 영역
        self.cart_frame = ttk.LabelFrame(self.main_frame, text="장바구니", padding="10")
        self.cart_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.display_menu()
        
    def display_menu(self):
        row = 0
        for category, items in self.menu_items.items():
            ttk.Label(self.menu_frame, text=category, font=('Helvetica', 12, 'bold')).grid(row=row, column=0, pady=5)
            row += 1
            
            for item, price in items.items():
                ttk.Label(self.menu_frame, text=f"{item} - {price}원").grid(row=row, column=0, pady=2)
                ttk.Button(self.menu_frame, text="추가", 
                          command=lambda i=item, p=price: self.add_to_cart(i, p)).grid(row=row, column=1)
                row += 1
    
    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        self.update_cart_display()
    
    def update_cart_display(self):
        # 기존 장바구니 표시 내용 삭제
        for widget in self.cart_frame.winfo_children():
            widget.destroy()
            
        # 장바구니 내용 표시
        row = 0
        total = 0
        for item, price in self.cart:
            ttk.Label(self.cart_frame, text=f"{item} - {price}원").grid(row=row, column=0, pady=2)
            row += 1
            total += price
        
        ttk.Label(self.cart_frame, text=f"총액: {total}원", font=('Helvetica', 12, 'bold')).grid(row=row, column=0, pady=5)
        ttk.Button(self.cart_frame, text="결제하기", command=self.checkout).grid(row=row+1, column=0, pady=5)
    
    def checkout(self):
        # 결제 로직 구현 예정
        print("결제가 완료되었습니다.")
        self.cart = []
        self.update_cart_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = KioskApp(root)
    root.mainloop() 