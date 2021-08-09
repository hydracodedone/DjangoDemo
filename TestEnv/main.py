import json
import os

import django

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FirstProject.settings")
    django.setup()

    from AppleApp.models import AppleInstance
    from AppleApp.serializers.readSerializer.apple import AppleInstanceReadSerializer

    obj = AppleInstance.objects.all()
    s = AppleInstanceReadSerializer(obj, many=True)
    print(json.dumps(s.data, ensure_ascii=False))
