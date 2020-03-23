import os, requests, shutil


class GenerateFiles:
    def main(self):
        template = './template.py'
        print("対象コンテスト名を入力してください(例:ABC155,ARC042,AGC032 等)")
        contest = input()

        # r = requests.get(url)
        # print(r.text)
        contest_name = contest[0:3]
        contest_name = contest_name.upper()
        if contest_name in ['ABC', 'ARC', 'AGC']:
            folder = f'../../{contest_name}/{contest}/'
        else:
            folder = f'../../others/{contest}/'

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
        for c in ['A', 'B', 'C', 'D', 'E', 'F']:
            file_path = f'{folder}{c}.py'
            if os.path.exists(file_path):
                print(f'{c}:ファイルが既に存在しています')
            else:
                if use_template:
                    shutil.copy2(template,file_path)
                    print(f'{folder}{c}.py を生成しました')
                else:
                    f = open(file_path, 'w')
                    f.close()
                    print(f'{folder}{c}.py を生成しました')


if __name__ == '__main__':
    GenerateFiles().main()
