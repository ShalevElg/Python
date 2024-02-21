import re

def check_password_strength(password):
    # קריטריונים
    min_length = 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    common_words = ["admin", "123456", "password"]

    # בדיקת אורך
    length_score = min(1, len(password) / min_length)

    # בדיקת הופעת תווים מיוחדים
    special_char_score = 1 if has_special else 0.5

    # בדיקת הופעת אותיות גדולות וקטנות
    case_score = 1 if has_upper and has_lower else 0.5

    # בדיקת הופעת מספרים
    digit_score = 1 if has_digit else 0.5

    # בדיקת הופעת מילים נפוצות
    common_word_score = 0
    for common_word in common_words:
        if common_word in password:
            common_word_score -= 1

    # חיבור הציונים
    total_score = length_score + special_char_score + case_score + digit_score + common_word_score

    # סיווג הסיסמה לפי הציון
    if total_score >= 4:
        strength = "חזקה"
    elif total_score >= 3:
        strength = "בינונית"
    else:
        strength = "חלשה"

    return strength

def main():
    password = input("הזן סיסמה: ")
    strength = check_password_strength(password)
    print(f"עוצמת הסיסמה היא: {strength}")

if __name__ == "__main__":
    main()