import os, requests


class GenerateFiles:
    def main(self):
        print("対象コンテスト名を入力してください(例:ABC155, AGC032 等)")
        contest = input()

        # r = requests.get(url)
        # print(r.text)
        contest_name = contest[0:3]
        contest_name = contest_name.upper()
        folder = f'../{contest_name}/{contest}/'
        if contest_name in ['ABC', 'ARC', 'AGC']:
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
                    f = open(file_path,'w')
                    f.close()


if __name__ == '__main__':
    GenerateFiles().main()
