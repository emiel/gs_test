class CombinationRestriction:
    pass


def project_type_allowed_on_lane(project_type_a, lane):
    project_types = [int(samples["project_type"]) for samples in lane]
    crs = CombinationRestriction.objects.all()
    project_type_a = int(project_type_a)
    for cr in crs:
        for project_type_b in project_types:
            if project_type_a == project_type_b:
                return True
        if (project_type_b == cr.project_type1) and (
            project_type_a != cr.project_type2
        ):
            for cr2 in crs:
                if (project_type_b == cr2.project_type1) and (
                    project_type_a == cr2.project_type2
                ):
                    return True
            return False
    return True
