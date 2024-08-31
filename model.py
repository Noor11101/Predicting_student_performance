from pycaret.classification import load_model, predict_model
import pandas as pd

# تحميل النموذج المدرب
model = load_model("student_performance_api")

def make_prediction(**kwargs):
    # تحويل البيانات إلى DataFrame
    df = pd.DataFrame([kwargs])
    
    # إجراء التنبؤ
    predictions = predict_model(model, data=df)
    
    # استخراج التنبؤ
    predicted_grade = predictions["prediction_label"].iloc[0]
    grade_map = {
        0: 'ممتاز (90-100%)',
        1: 'جيد جدًا (80-89%)',
        2: 'جيد (70-79%)',
        3: 'مقبول (60-69%)',
        4: 'راسب (أقل من 60%)'
    }
    grade = grade_map.get(predicted_grade, 'غير معروف')
    
    return {"الدرجة المتوقعة": grade}