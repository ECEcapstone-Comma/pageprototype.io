import csv
from sangsi.models import Audition

def save_auditions_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # 첫 번째 행은 헤더이므로 건너뜁니다.
        for row in reader:
            planning_agency = row[0]
            audition_name = row[0]
            age_group1 = int(row[1])
            age_group2 = int(row[2])
            recruitment_field = row[3]
            gender = row[4]
            url = row[5]
            data_number = row[7]

            
            # 데이터 모델 객체 생성 및 필드 값 할당
            jungi_audition_data = Audition(
                planning_agency=planning_agency,
                audition_name=audition_name,
                recruitment_field=recruitment_field,
                age_group1=age_group1,
                age_group2=age_group2,
                gender=gender,
                url=url,
                data_number=data_number,
            )
            
            # 객체 저장
            jungi_audition_data.save()
