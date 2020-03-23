import os, requests, shutil

is_create_tests = True  # テストファイルを生成しない場合はFalseに


class GenerateFiles:
    def main(self):
        template = './template.py'
        create_count = 6  # 生成するファイルの数
        questions = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        print("対象コンテスト名を入力してください(例:ABC155,ARC042,AGC032 等)")
        contest = input()

        # r = requests.get(url)
        # print(r.text)
        contest_name = contest[0:3]
        contest_name = contest_name.upper()
        if contest_name in ['ABC', 'ARC', 'AGC']:
            folder = f'../../{contest_name}/{contest}/'
            if contest_name == 'ABC' and int(contest[3:]) < 126:
                create_count = 4
            if contest_name == 'ARC':
                create_count = 4
        else:
            contest_name = 'others'
            folder = f'../../{contest_name}/{contest}/'
            print('問題は何問ですか？　4:Dまで、6:Fまで、10:J、25:Zまでを生成します（最大25問）')
            create_count = int(input())
            print(f'A~{questions[create_count - 1]}問題で作成します')
        use_template = False
        if os.path.isfile(template):
            print('テンプレートを使用します')
            use_template = True
        print(f'{folder}を作成します。よろしいですか？[Y/N]')
        yn = input()
        if yn != 'Y':
            print('終了します')
            exit()
        # フォルダが無い場合は作成する
        if os.path.exists(folder):
            print(f'既にフォルダが存在しています({folder})')
        else:
            os.mkdir(folder)
            print(f'{folder}を作成しました')

        for i in range(create_count):
            c = questions[i]
            file_path = f'{folder}{c}.py'
            test_path = f'{folder}{c}_test.py'
            # ファイルの生成
            if os.path.exists(file_path):
                print(f'{c}:ファイルが既に存在しています')
            else:
                if use_template:
                    shutil.copy2(template, file_path)
                    print(f'{folder}{c}.py を生成しました')
                else:
                    f = open(file_path, 'w')
                    f.close()
                    print(f'{folder}{c}.py を生成しました')
            # テストの生成
            if os.path.exists(test_path):
                print(f'{c}_test:ファイルが既に存在しています')
            else:
                f = open(test_path, 'w')
                lines = f'def resolve():\n'
                lines += f'\tfrom {contest_name}.{contest} import {c}\n'
                lines += f'\t{c}.main()'
                f.write(lines)
                f.close()
                print(f'{folder}{c}_test.py を生成しました')


if __name__ == '__main__':
    GenerateFiles().main()
