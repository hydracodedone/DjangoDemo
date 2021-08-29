from AppleApp.models import AppleType, AppleLevel, AppleMaturity, ApplePesticideResidue, ApplePackingType


class AppleFeatureModelAction(object):
    @staticmethod
    def query_all_apple_feature_info():
        result = {
            "apple_type": AppleType.custom_objects.all(),
            "apple_level": AppleLevel.custom_objects.all(),
            "apple_maturity": AppleMaturity.custom_objects.all(),
            "apple_pesticide_residue": ApplePesticideResidue.custom_objects.all(),
            "apple_packing_type": ApplePackingType.custom_objects.all(),
        }
        return result
