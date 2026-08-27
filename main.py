import flet as ft

def main(page: ft.Page):
    page.title = "حل مشكلة النوافذ - Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # دالة إغلاق النافذة بطريقة سليمة وآمنة
    def close_dialog(e):
        dialog.open = False
        page.dialog = None  # تفريغ النافذة لمنع تعليقها في الواجهة
        page.update()

    # إنشاء النافذة المنبثقة (AlertDialog)
    dialog = ft.AlertDialog(
        title=ft.Text("تنبيه هام"),
        content=ft.Text("تم حل مشكلة إغلاق النوافذ بنجاح!"),
        actions=[
            ft.TextButton("إغلاق", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # دالة فتح النافذة
    def open_dialog(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    # زر في الصفحة الرئيسية لفتح النافذة
    page.add(
        ft.ElevatedButton(
            text="اضغط لفتح النافذة",
            on_click=open_dialog
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
