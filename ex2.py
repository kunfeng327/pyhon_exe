from docx import Document
from docx.shared import RGBColor

def find_word_style():
    try:
        # ===================== 这里改成你的文件路径 =====================
        doc = Document("test.docx")  
        # ===============================================================
    except:
        print("❌ 未找到 test.docx 文件")
        return

    red_texts = []       # 纯红色
    bold_texts = []      # 纯加粗
    red_bold_texts = []  # 红+粗

    last_is_red = False
    last_is_bold = False
    current_text = ""

    # 遍历所有文字
    for para in doc.paragraphs:
        for run in para.runs:
            text = run.text.strip()
            if not text:
                continue

            # 判断颜色和加粗
            is_red = (run.font.color.rgb == RGBColor(255, 0, 0))
            is_bold = run.bold if run.bold is not None else False

            # 相同格式 → 合并文字（解决 w + wer 变成两段的问题）
            if is_red == last_is_red and is_bold == last_is_bold:
                current_text += text
            else:
                if current_text:
                    # 全部用 if，不用 elif
                    if last_is_red:
                        red_texts.append(current_text)
                    if last_is_bold:
                        bold_texts.append(current_text)
                    if last_is_red and last_is_bold:
                        red_bold_texts.append(current_text)

                current_text = text
                last_is_red = is_red
                last_is_bold = is_bold

    # 最后一段也要加进去
    if current_text:
        if last_is_red:
            red_texts.append(current_text)
        if last_is_bold:
            bold_texts.append(current_text)
        if last_is_red and last_is_bold:
            red_bold_texts.append(current_text)

    # ===================== 输出结果 =====================
    print("=" * 40)
    print("📕 红色文本：")
    print("\n".join(f"- {t}" for t in red_texts) if red_texts else "无")

    print("\n📌 加粗文本：")
    print("\n".join(f"- {t}" for t in bold_texts) if bold_texts else "无")

    print("\n🔴 同时红色+加粗文本：")
    print("\n".join(f"- {t}" for t in red_bold_texts) if red_bold_texts else "无")
    print("=" * 40)

find_word_style()