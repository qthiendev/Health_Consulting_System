from django.shortcuts import render
import os
import google.generativeai as genai


def get_home_page(request):
    return render(request, 'HomePage.html')

def calculate_bmi(weight, height):
    if height <= 0:
        return None  # To avoid division by zero
    return weight / ((height/100) ** 2)

def get_bmi_page(request):
    weight = None
    height = None
    bmi = None
    message = ""

    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        try:
            if weight and height:
                weight = float(weight)
                height = float(height)
                bmi = calculate_bmi(weight, height)
                message = "Chỉ số BMI của bạn là: {:.2f}".format(bmi)
            else:
                message = "Vui lòng nhập cân nặng và chiều cao."
        except ValueError:
            message = "Cân nặng và chiều cao phải là số hợp lệ."

    return render(request, 'BMIPage.html', {
        'weight': weight,
        'height': height,
        'bmi': bmi,
        'message': message,
    })

# def generate_response(profile, user_question):
#     GERMINI_API = ""
#     medical_history = ', '.join(profile.medical_histories.values_list('item', flat=True))
#     prompt = f"Hiện tại tôi đang ở {profile.address}, cân nặng {profile.weight}, chiều cao {profile.height}, mức độ vận động {profile.exercise_level}, tiền sử bệnh lý {medical_history}. {user_question}"
    
#     genai.configure(api_key=GERMINI_API)
#     generation_config = {
#         "temperature": 1,
#         "top_p": 0.95,
#         "top_k": 64,
#         "max_output_tokens": 8192,
#         "response_mime_type": "text/plain",
#     }
    
#     model = genai.GenerativeModel(
#         model_name="gemini-1.5-flash",
#         generation_config=generation_config,
#         system_instruction="You are a bot that gives advice based on what user provides. Use all data you have, just give them advice, use all index like height, weight, exercise level, medical history. Use current addess of user to advise some local dishes. Provide with html tag.",
#     )
    
#     chat_session = model.start_chat(
#         history=[
#             {
#                 "role": "user",
#                 "parts": [
#                     "Hiện tại tôi đang ở K318/17 Tôn Đản, Hòa An, Cẩm Lệ, Đà Nẵng, cân nặng 71.0, chiều cao 171.0, mức độ vận động sedentary, tiền sử bệnh lý Thiếu máu lên não, Hạn chế tiêu thụ đạm. Trưa nay tôi nên ăn gì",
#                 ],
#             },
#             {
#                 "role": "model",
#                 "parts": [
#                     "Dựa vào thông tin bạn cung cấp, tôi khuyên bạn nên ăn nhẹ nhàng và dễ tiêu hóa vào buổi trưa. \n\n<strong>Gợi ý:</strong>\n\n* Cháo: Cháo trắng, cháo cá lóc, cháo gà, cháo tôm... là những lựa chọn tốt cho bữa trưa. \n* Canh: Canh khổ qua nhồi thịt, canh rau cải nấu tôm, canh mướp nấu thịt bằm... bổ sung vitamin và khoáng chất.\n* Món luộc: Thịt luộc, cá luộc, rau luộc... ít dầu mỡ, dễ tiêu hóa.\n* Bánh mì: Bánh mì kẹp thịt, bánh mì ốp la, bánh mì chảo... có thể bổ sung thêm rau xanh.\n\n<strong>Lưu ý:</strong>\n\n* Nên hạn chế ăn các món nhiều dầu mỡ, cay nóng.\n* Uống nhiều nước lọc, nước ép trái cây.\n* Tăng cường rau xanh và trái cây trong khẩu phần ăn.\n* <strong>Nên tham khảo ý kiến bác sĩ để được tư vấn về chế độ ăn uống phù hợp với tình trạng sức khỏe.</strong>\n\n<strong>Món ăn đặc sản địa phương:</strong>\n\n* Bún chả cá: Món ăn nổi tiếng của Đà Nẵng, nước dùng thanh ngọt, chả cá dai ngon. \n* Bánh tráng cuốn thịt heo: Món ăn vặt được nhiều người yêu thích, dễ ăn, dễ tiêu hóa.\n* Mì Quảng: Món ăn đặc trưng của miền Trung, nước dùng đậm đà, sợi mì dai ngon.\n\nĐịa chỉ tham khảo:\n\n* Quán bún chả cá Thuận Phát: K316/73 Tôn Đản, Hòa An, Cẩm Lệ, Đà Nẵng.\n* Quán bánh tráng cuốn thịt heo Cô Hoa: K318/34 Tôn Đản, Hòa An, Cẩm Lệ, Đà Nẵng.\n* Quán mì Quảng Bà Mười: K318/45 Tôn Đản, Hòa An, Cẩm Lệ, Đà Nẵng. \n\nBạn có thể tìm hiểu thêm về các món ăn địa phương và địa chỉ quán ăn qua các ứng dụng đặt đồ ăn như GrabFood, Now, Foody,...\n\n<strong>Chúc bạn ngon miệng!</strong>\n",
#                 ],
#             },
#         ]
#     )
    
#     response = chat_session.send_message(prompt)
#     return response.text     

def get_chatbot_page(request):
    # response = ''
    # if request.method == 'POST':
    #     user_question = request.POST.get('user_question')
    #     profile = request.user.profile
    #     response = generate_response(profile, user_question)
    return render(request, 'Chatbot.html', {'response': "Dựa vào thông tin bạn cung cấp, tôi khuyên bạn nên ăn nhẹ nhàng và dễ tiêu hóa vào buổi trưa. \n\n<strong>Gợi ý:</strong>\n\n* Cháo: Cháo trắng, cháo cá lóc, cháo gà, cháo tôm... là những lựa chọn tốt cho bữa trưa. \n* Canh: Canh khổ qua nhồi thịt, canh rau cải nấu tôm, canh mướp nấu thịt bằm... bổ sung vitamin và khoáng chất.* Món luộc: Thịt luộc, cá luộc, rau luộc... ít dầu mỡ, dễ tiêu hóa.\n* Bánh mì: Bánh mì kẹp thịt, bánh mì ốp la, bánh mì chảo... có thể bổ sung thêm rau xanh.\<strong>Lưu ý:</strong>* Nên hạn chế ăn các món nhiều dầu mỡ, cay nóng.\n* Uống nhiều nước lọc, nước ép trái cây.\n* Tăng cường rau xanh và trái cây trong khẩu phần ăn.\n* <strong>Nên tham khảo ý kiến bác sĩ để được tư vấn về chế độ ăn uống phù hợp với tình trạng sức khỏe.</strong>\n\n<strong>Món ăn đặc sản địa phương:</strong>\n\n* Bún chả cá: Món ăn nổi tiếng của Đà Nẵng, nước dùng thanh ngọt, chả cá dai ngon. \n* Bánh tráng cuốn thịt heo: Món ăn vặt được nhiều người yêu thích, dễ ăn, dễ tiêu hóa.\n* Mì Quảng: Món ăn đặc trưng của miền Trung, nước dùng đậm đà, sợi mì dai ngon.\n\nĐịa chỉ tham khảo:\n\n* Quán bún chả cá Thuận Phát: K316/73 Tôn Đản, Hòa An, Cẩm Lệ, Đà Nẵng.\n* Quán bánh tráng cuốn thịt heo Cô Hoa: K318/34 Tôn Đản, Hòa An, Cẩm Lệ, Đà Nẵng.\n* Quán mì Quảng Bà Mười: K318/45 Tôn Đản, Hòa An, Cẩm Lệ, Đà Nẵng. \n\nBạn có thể tìm hiểu thêm về các món ăn địa phương và địa chỉ quán ăn qua các ứng dụng đặt đồ ăn như GrabFood, Now, Foody,...\n\n<strong>Chúc bạn ngon miệng!</strong>\n"})

