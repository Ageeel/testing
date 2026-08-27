import flet as ft

def main(page: ft.Page):
    page.title = "حل مشكلة النوافذ - Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. إنشاء النافذة المنبثقة
    dialog = ft.AlertDialog(
        title=ft.Text("تنبيه هام"),
        content=ft.Text("تم حل مشكلة إغلاق النوافذ بنجاح!"),
        actions=[
            ft.TextButton(content=ft.Text("إغلاق"), on_click=lambda e: close_dialog()),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # 2. دالة إغلاق النافذة بشكل آمن
    def close_dialog():
        dialog.open = False
        page.update()

    # 3. دالة فتح النافذة (يتم إسنادها لـ page.dialog وتحديث الصفحة)
    def open_dialog(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    # 4. الزر الرئيسي في الصفحة
    page.add(
        ft.ElevatedButton(
            content=ft.Text("اضغط لفتح النافذة"),
            on_click=open_dialog
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
