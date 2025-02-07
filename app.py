from flask import Flask, request, render_template_string

app = Flask(__name__)

# rules_data.py (hoặc chung file với Flask)

rules = [
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo phông",
            "Quần jeans",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo ba lỗ",
            "Quần short thể thao",
            "Giày chạy bộ"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo sơ mi",
            "Quần âu",
            "Giày tây"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác da",
            "Quần skinny",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Vest cổ điển",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo polo",
            "Quần kaki",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nam",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo hoodie",
            "Quần cargo",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "don_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo thun",
            "Quần culottes",
            "Dép sandals"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "nang_dong",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo croptop",
            "Quần short",
            "Giày thể thao"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "thanh_lich",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Blouse",
            "Váy midi",
            "Giày cao gót"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "ca_tinh",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo khoác bomber",
            "Quần jean rách",
            "Giày boots"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "co_dien",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Đầm vintage",
            "Giày búp bê",
            "Túi da nhỏ"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "toi_gian",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo len",
            "Quần âu",
            "Giày lười"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "nong",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "lanh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "gio_manh",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "co",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "khong_co",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "tiec",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "trang_trong",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "lich_su",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    },
    {
        "gioitinh": "nu",
        "phongcach": "duong_pho",
        "thoitiet": "am_thap",
        "hoatdong": "khong",
        "sukien": "hoi_nghi",
        "quydinh": "khong_quy_dinh",
        "recommendations": [
            "Áo oversize",
            "Quần baggy",
            "Sneakers"
        ]
    }
]

def match_rule(rule, g, p, t, h, s, q):
    """
    Kiểm tra xem (g, p, t, h, s, q) 
    có nằm trong list mỗi trường của rule hay không.
    """
    if g not in rule["gioitinh"]:
        return False
    if p not in rule["phongcach"]:
        return False
    if t not in rule["thoitiet"]:
        return False
    if h not in rule["hoatdong"]:
        return False
    if s not in rule["sukien"]:
        return False
    if q not in rule["quydinh"]:
        return False
    return True

def get_outfit(gioitinh, phongcach, thoitiet, hoatdong, sukien, quydinh):
    for rule in rules:
        if match_rule(rule, gioitinh, phongcach, thoitiet, hoatdong, sukien, quydinh):
            return rule["recommendations"]
    # fallback
    return ["(Không tìm thấy gợi ý phù hợp)"]

# ===================
# HTML TRANG FORM
# ===================
index_html = """
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Hệ Chuyên Gia Gợi Ý Trang Phục</title>
  <link 
    rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
  >
</head>
<body class="bg-light">
  <div class="container py-4">
    <h1>Chọn Tiêu Chí Trang Phục</h1>
    <form action="/result" method="POST" class="row g-3">

      <!-- 1. Giới tính -->
      <div class="col-md-6">
        <label class="form-label">Giới tính</label>
        <select name="gioitinh" class="form-select">
          <option value="nam">Nam</option>
          <option value="nu">Nữ</option>
        </select>
      </div>

      <!-- 2. Phong cách -->
      <div class="col-md-6">
        <label class="form-label">Phong cách</label>
        <select name="phongcach" class="form-select">
          <option value="don_gian">Đơn giản</option>
          <option value="nang_dong">Năng động</option>
          <option value="thanh_lich">Thanh lịch</option>
          <option value="ca_tinh">Cá tính</option>
          <option value="co_dien">Cổ điển</option>
          <option value="toi_gian">Tối giản</option>
          <option value="duong_pho">Đường phố</option>
        </select>
      </div>

      <!-- 3. Thời tiết -->
      <div class="col-md-6">
        <label class="form-label">Thời tiết</label>
        <select name="thoitiet" class="form-select">
          <option value="nong">Nóng</option>
          <option value="lanh">Lạnh</option>
          <option value="gio_manh">Gió mạnh</option>
          <option value="am_thap">Ẩm thấp</option>
        </select>
      </div>

      <!-- 4. Hoạt động ngoài trời -->
      <div class="col-md-6">
        <label class="form-label">Hoạt động ngoài trời</label>
        <select name="hoatdong" class="form-select">
          <option value="co">Có</option>
          <option value="khong">Không</option>
        </select>
      </div>

      <!-- 5. Sự kiện -->
      <div class="col-md-6">
        <label class="form-label">Sự kiện</label>
        <select name="sukien" class="form-select">
          <option value="khong_co">Không có</option>
          <option value="tiec">Tiệc</option>
          <option value="hoi_nghi">Hội nghị</option>
        </select>
      </div>

      <!-- 6. Quy định trang phục -->
      <div class="col-md-6">
        <label class="form-label">Quy định trang phục</label>
        <select name="quydinh" class="form-select">
          <option value="trang_trong">Trang trọng</option>
          <option value="lich_su">Lịch sự</option>
          <option value="khong_quy_dinh">Không quy định</option>
        </select>
      </div>

      <div class="col-12 mt-4">
        <button type="submit" class="btn btn-primary">Xem gợi ý</button>
      </div>
    </form>
  </div>

  <script 
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js">
  </script>
</body>
</html>
"""

# ===================
# HTML TRANG KẾT QUẢ
# ===================
result_html = """
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Kết Quả Gợi Ý</title>
  <link 
    rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
  >
</head>
<body class="bg-light">
  <div class="container py-4">
    <h2 class="mb-3">Kết Quả Gợi Ý</h2>

    <div class="mb-4">
      <h5>Các lựa chọn của bạn:</h5>
      <ul>
        <li>Giới tính: {{ gioitinh }}</li>
        <li>Phong cách: {{ phongcach }}</li>
        <li>Thời tiết: {{ thoitiet }}</li>
        <li>Hoạt động ngoài trời: {{ hoatdong }}</li>
        <li>Sự kiện: {{ sukien }}</li>
        <li>Quy định trang phục: {{ quydinh }}</li>
      </ul>
    </div>

    <div class="mb-4">
      <h5>Gợi ý bộ trang phục:</h5>
      <ul>
        {% for item in outfit %}
          <li>{{ item }}</li>
          <p>{{ item.name }}</p>
        <div class="outfit-item">
        <p>{{ item.name }}</p>
        <a href="https://www.google.com/search?hl=vi&tbm=isch&q={{ item.name | replace(' ', '+') }}" target="_blank">Tìm trên Google</a> |
        </div>

        {% endfor %}
      </ul>
    </div>
    <a href="/" class="btn btn-secondary">Quay về</a>
    
  </div>

  <script 
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js">
  </script>
</body>
</html>
"""

# ===================
# ROUTES FLASK
# ===================
@app.route("/", methods=["GET"])
def index():
    # Trả về HTML form bằng render_template_string
    return render_template_string(index_html)

@app.route("/result", methods=["POST"])
def result():
    # Lấy dữ liệu
    gioitinh   = request.form.get("gioitinh", "")
    phongcach  = request.form.get("phongcach", "")
    thoitiet   = request.form.get("thoitiet", "")
    hoatdong   = request.form.get("hoatdong", "")
    sukien     = request.form.get("sukien", "")
    quydinh    = request.form.get("quydinh", "")

    # Gọi hàm get_outfit để tìm rule
    outfit = get_outfit(gioitinh, phongcach, thoitiet, hoatdong, sukien, quydinh)

    # Trả về kết quả
    return render_template_string(result_html,
        outfit=outfit,
        gioitinh=gioitinh,
        phongcach=phongcach,
        thoitiet=thoitiet,
        hoatdong=hoatdong,
        sukien=sukien,
        quydinh=quydinh
    )

if __name__ == "__main__":
    app.run(debug=True)
