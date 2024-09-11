import os
import csv


def main():
    base_dir = '.'
    csv_file = 'output_0911_n3.csv'
    columns = ['编号', '标签', '题目概述', '输入', '输出（deepseekv2_5）', '输出（gpt_4o_20240513ptu）', '输出（qwen2_72b_instruct）', '输出（ours_0829_pretrain_full）', '输出（ours_0829_pretrain_half）']
    #columns = ['编号', '标签', '题目概述', '输入', '输出（deepseekv2_5）', '输出（gpt_4o_20240513ptu）', '输出（qwen2_72b_instruct）', '指令（instruct）输入']

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()

    for folder in sorted(os.listdir(base_dir)):
        if folder.startswith('.') or folder.endswith('.csv') or folder in ['tmp']:
            continue

        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        number, label, summary = folder.split('_')

        base_file = os.path.join(folder_path, 'base.txt')
        with open(base_file, 'r', encoding='utf-8') as f:
            instruct = f.read().strip()

        completion_path = os.path.join(folder_path, 'completion')
        input_file = os.path.join(completion_path, 'input.txt')
        deepseek_file = os.path.join(completion_path, 'output_deepseekv2_5.txt')
        gpt_file = os.path.join(completion_path, 'output_gpt_4o_20240513ptu.txt')
        qwen_file = os.path.join(completion_path, 'output_qwen2_72b_instruct.txt')
        ours_0829_pretrain_full_file = os.path.join(completion_path, "output_internlm25_fullpt_0829_2100M_filterd_codemath_360M_fullprompt.txt")
        ours_0829_pretrain_half_file = os.path.join(completion_path,"output_internlm25_fullpt_0829_2100M_filterd_codemath_360M_halfprompt.txt")

        with open(input_file, 'r', encoding='utf-8') as f:
            input_text = f.read().strip()

        with open(deepseek_file, 'r', encoding='utf-8') as f:
            deepseek_output = f.read().strip()

        with open(gpt_file, 'r', encoding='utf-8') as f:
            gpt_output = f.read().strip()

        with open(qwen_file, 'r', encoding='utf-8') as f:
            qwen_output = f.read().strip()
        
        with open(ours_0829_pretrain_full_file, 'r', encoding='utf-8') as f:
            ours_0829_pretrain_full_output = f.read().strip()

        with open(ours_0829_pretrain_half_file, 'r', encoding='utf-8') as f:
            ours_0829_pretrain_half_output = f.read().strip()


        row = {
            '编号': number,
            '标签': label,
            '题目概述': summary,
            '输入': input_text,
            '输出（deepseekv2_5）': deepseek_output,
            '输出（gpt_4o_20240513ptu）': gpt_output,
            '输出（qwen2_72b_instruct）': qwen_output,
            '输出（ours_0829_pretrain_full）': ours_0829_pretrain_full_output,
            '输出（ours_0829_pretrain_half）': ours_0829_pretrain_half_output
            #'指令（instruct）输入': instruct,
        }

        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writerow(row)

    print(f"CSV文件已生成: {csv_file}")


if __name__ == "__main__":
    main()
