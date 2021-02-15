from canary_sniffer.sniffers import CanarySniffer


def property_has_septic(address, zipcode):
    has_septic = CanarySniffer().has_septic(address, zipcode)

    # Can add logic here for future website scrapers that try to answer the same question.

    return {"address": address,
            "zipcode": zipcode,
            "has_septic": has_septic}
