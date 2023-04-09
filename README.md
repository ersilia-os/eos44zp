# CYP450 metabolism

Analysis of metabolic stability, determining the inhibition of CYP450 activity and whether the compounds are a substrate for the CYP450 enzimes. The data to build these models is publicly available at PubChem, AID1645840, AID1645841, AID1645842. The tested cyps include CYP2C9, CYP2D6 and CYP3A4.

## Identifiers

* EOS model ID: `eos44zp`
* Slug: `ncats-cyp450`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Probability of inhibiting the enzyme and probability of being a ubstrate of the enzyme. Activity in both indicates the compound is a ligand of the enzyme.

## References

* [Publication](https://dmd.aspetjournals.org/content/49/9/822)
* [Source Code](https://github.com/ncats/ncats-adme)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Citation

If you use this model, please cite the [original authors](https://dmd.aspetjournals.org/content/49/9/822) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!