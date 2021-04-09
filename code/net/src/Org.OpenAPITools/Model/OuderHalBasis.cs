/* 
 * Bevragen Ingeschreven Personen
 *
 * API voor het bevragen van ingeschreven personen uit de basisregistratie personen (BRP), inclusief de registratie niet-ingezeten (RNI). Met deze API kun je personen zoeken en actuele gegevens over personen, kinderen, partners en ouders raadplegen.  Gegevens die er niet zijn of niet actueel zijn krijg je niet terug. Heeft een persoon bijvoorbeeld geen geldige nationaliteit, en alleen een beëindigd partnerschap, dan krijg je geen gegevens over nationaliteit en partner.  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/tree/v1.1.0/features) voor nadere toelichting. 
 *
 * The version of the OpenAPI document: 1.3.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// OuderHalBasis
    /// </summary>
    [DataContract]
    public partial class OuderHalBasis :  IEquatable<OuderHalBasis>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="OuderHalBasis" /> class.
        /// </summary>
        /// <param name="burgerservicenummer">burgerservicenummer.</param>
        /// <param name="geslachtsaanduiding">geslachtsaanduiding.</param>
        /// <param name="ouderAanduiding">ouderAanduiding.</param>
        /// <param name="datumIngangFamilierechtelijkeBetrekking">datumIngangFamilierechtelijkeBetrekking.</param>
        /// <param name="naam">naam.</param>
        /// <param name="inOnderzoek">inOnderzoek.</param>
        /// <param name="geboorte">geboorte.</param>
        /// <param name="geheimhoudingPersoonsgegevens">Gegevens mogen niet worden verstrekt aan derden / maarschappelijke instellingen. .</param>
        /// <param name="links">links.</param>
        public OuderHalBasis(string burgerservicenummer = default(string), GeslachtEnum geslachtsaanduiding = default(GeslachtEnum), OuderAanduidingEnum ouderAanduiding = default(OuderAanduidingEnum), DatumOnvolledig datumIngangFamilierechtelijkeBetrekking = default(DatumOnvolledig), Naam naam = default(Naam), OuderInOnderzoek inOnderzoek = default(OuderInOnderzoek), Geboorte geboorte = default(Geboorte), bool geheimhoudingPersoonsgegevens = default(bool), OuderLinks links = default(OuderLinks))
        {
            this.Burgerservicenummer = burgerservicenummer;
            this.Geslachtsaanduiding = geslachtsaanduiding;
            this.OuderAanduiding = ouderAanduiding;
            this.DatumIngangFamilierechtelijkeBetrekking = datumIngangFamilierechtelijkeBetrekking;
            this.Naam = naam;
            this.InOnderzoek = inOnderzoek;
            this.Geboorte = geboorte;
            this.GeheimhoudingPersoonsgegevens = geheimhoudingPersoonsgegevens;
            this.Links = links;
        }
        
        /// <summary>
        /// Gets or Sets Burgerservicenummer
        /// </summary>
        [DataMember(Name="burgerservicenummer", EmitDefaultValue=false)]
        public string Burgerservicenummer { get; set; }

        /// <summary>
        /// Gets or Sets Geslachtsaanduiding
        /// </summary>
        [DataMember(Name="geslachtsaanduiding", EmitDefaultValue=false)]
        public GeslachtEnum Geslachtsaanduiding { get; set; }

        /// <summary>
        /// Gets or Sets OuderAanduiding
        /// </summary>
        [DataMember(Name="ouderAanduiding", EmitDefaultValue=false)]
        public OuderAanduidingEnum OuderAanduiding { get; set; }

        /// <summary>
        /// Gets or Sets DatumIngangFamilierechtelijkeBetrekking
        /// </summary>
        [DataMember(Name="datumIngangFamilierechtelijkeBetrekking", EmitDefaultValue=false)]
        public DatumOnvolledig DatumIngangFamilierechtelijkeBetrekking { get; set; }

        /// <summary>
        /// Gets or Sets Naam
        /// </summary>
        [DataMember(Name="naam", EmitDefaultValue=false)]
        public Naam Naam { get; set; }

        /// <summary>
        /// Gets or Sets InOnderzoek
        /// </summary>
        [DataMember(Name="inOnderzoek", EmitDefaultValue=false)]
        public OuderInOnderzoek InOnderzoek { get; set; }

        /// <summary>
        /// Gets or Sets Geboorte
        /// </summary>
        [DataMember(Name="geboorte", EmitDefaultValue=false)]
        public Geboorte Geboorte { get; set; }

        /// <summary>
        /// Gegevens mogen niet worden verstrekt aan derden / maarschappelijke instellingen. 
        /// </summary>
        /// <value>Gegevens mogen niet worden verstrekt aan derden / maarschappelijke instellingen. </value>
        [DataMember(Name="geheimhoudingPersoonsgegevens", EmitDefaultValue=false)]
        public bool GeheimhoudingPersoonsgegevens { get; set; }

        /// <summary>
        /// Gets or Sets Links
        /// </summary>
        [DataMember(Name="_links", EmitDefaultValue=false)]
        public OuderLinks Links { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class OuderHalBasis {\n");
            sb.Append("  Burgerservicenummer: ").Append(Burgerservicenummer).Append("\n");
            sb.Append("  Geslachtsaanduiding: ").Append(Geslachtsaanduiding).Append("\n");
            sb.Append("  OuderAanduiding: ").Append(OuderAanduiding).Append("\n");
            sb.Append("  DatumIngangFamilierechtelijkeBetrekking: ").Append(DatumIngangFamilierechtelijkeBetrekking).Append("\n");
            sb.Append("  Naam: ").Append(Naam).Append("\n");
            sb.Append("  InOnderzoek: ").Append(InOnderzoek).Append("\n");
            sb.Append("  Geboorte: ").Append(Geboorte).Append("\n");
            sb.Append("  GeheimhoudingPersoonsgegevens: ").Append(GeheimhoudingPersoonsgegevens).Append("\n");
            sb.Append("  Links: ").Append(Links).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as OuderHalBasis);
        }

        /// <summary>
        /// Returns true if OuderHalBasis instances are equal
        /// </summary>
        /// <param name="input">Instance of OuderHalBasis to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(OuderHalBasis input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Burgerservicenummer == input.Burgerservicenummer ||
                    (this.Burgerservicenummer != null &&
                    this.Burgerservicenummer.Equals(input.Burgerservicenummer))
                ) && 
                (
                    this.Geslachtsaanduiding == input.Geslachtsaanduiding ||
                    (this.Geslachtsaanduiding != null &&
                    this.Geslachtsaanduiding.Equals(input.Geslachtsaanduiding))
                ) && 
                (
                    this.OuderAanduiding == input.OuderAanduiding ||
                    (this.OuderAanduiding != null &&
                    this.OuderAanduiding.Equals(input.OuderAanduiding))
                ) && 
                (
                    this.DatumIngangFamilierechtelijkeBetrekking == input.DatumIngangFamilierechtelijkeBetrekking ||
                    (this.DatumIngangFamilierechtelijkeBetrekking != null &&
                    this.DatumIngangFamilierechtelijkeBetrekking.Equals(input.DatumIngangFamilierechtelijkeBetrekking))
                ) && 
                (
                    this.Naam == input.Naam ||
                    (this.Naam != null &&
                    this.Naam.Equals(input.Naam))
                ) && 
                (
                    this.InOnderzoek == input.InOnderzoek ||
                    (this.InOnderzoek != null &&
                    this.InOnderzoek.Equals(input.InOnderzoek))
                ) && 
                (
                    this.Geboorte == input.Geboorte ||
                    (this.Geboorte != null &&
                    this.Geboorte.Equals(input.Geboorte))
                ) && 
                (
                    this.GeheimhoudingPersoonsgegevens == input.GeheimhoudingPersoonsgegevens ||
                    (this.GeheimhoudingPersoonsgegevens != null &&
                    this.GeheimhoudingPersoonsgegevens.Equals(input.GeheimhoudingPersoonsgegevens))
                ) && 
                (
                    this.Links == input.Links ||
                    (this.Links != null &&
                    this.Links.Equals(input.Links))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Burgerservicenummer != null)
                    hashCode = hashCode * 59 + this.Burgerservicenummer.GetHashCode();
                if (this.Geslachtsaanduiding != null)
                    hashCode = hashCode * 59 + this.Geslachtsaanduiding.GetHashCode();
                if (this.OuderAanduiding != null)
                    hashCode = hashCode * 59 + this.OuderAanduiding.GetHashCode();
                if (this.DatumIngangFamilierechtelijkeBetrekking != null)
                    hashCode = hashCode * 59 + this.DatumIngangFamilierechtelijkeBetrekking.GetHashCode();
                if (this.Naam != null)
                    hashCode = hashCode * 59 + this.Naam.GetHashCode();
                if (this.InOnderzoek != null)
                    hashCode = hashCode * 59 + this.InOnderzoek.GetHashCode();
                if (this.Geboorte != null)
                    hashCode = hashCode * 59 + this.Geboorte.GetHashCode();
                if (this.GeheimhoudingPersoonsgegevens != null)
                    hashCode = hashCode * 59 + this.GeheimhoudingPersoonsgegevens.GetHashCode();
                if (this.Links != null)
                    hashCode = hashCode * 59 + this.Links.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
