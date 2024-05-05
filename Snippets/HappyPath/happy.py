


if json_obj is not None:
    authors = json_obj.get("author")
    if authors is not None:
        for author in authors:
            orcid = self.om.normalise(author.get("ORCID"))
            if orcid is not None:
                result.add(orcid)

            