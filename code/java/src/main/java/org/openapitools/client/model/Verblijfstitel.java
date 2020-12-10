/*
 * Bevragen Ingeschreven Personen
 * API voor het bevragen van ingeschreven personen uit de basisregistratie personen (BRP), inclusief de registratie niet-ingezeten (RNI). Met deze API kun je personen zoeken en actuele gegevens over personen, kinderen, partners en ouders raadplegen.  Gegevens die er niet zijn of niet actueel zijn krijg je niet terug. Heeft een persoon bijvoorbeeld geen geldige nationaliteit, en alleen een beëindigd partnerschap, dan krijg je geen gegevens over nationaliteit en partner.  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/tree/v1.1.0/features) voor nadere toelichting. 
 *
 * The version of the OpenAPI document: 1.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.DatumOnvolledig;
import org.openapitools.client.model.VerblijfstitelInOnderzoek;
import org.openapitools.client.model.Waardetabel;

/**
 * Gegevens over de verblijfsrechtelijke status van de persoon. * **datumEinde**: Datum waarop de geldigheid van de gegevens over de verblijfstitel is beëindigd. * **datumIngang**: Datum waarop de gegevens over de verblijfstitel geldig zijn geworden. * **aanduiding** : Verblijfstiteltabel die aangeeft over welke verblijfsrechtelijke status de persoon beschikt. 
 */
@ApiModel(description = "Gegevens over de verblijfsrechtelijke status van de persoon. * **datumEinde**: Datum waarop de geldigheid van de gegevens over de verblijfstitel is beëindigd. * **datumIngang**: Datum waarop de gegevens over de verblijfstitel geldig zijn geworden. * **aanduiding** : Verblijfstiteltabel die aangeeft over welke verblijfsrechtelijke status de persoon beschikt. ")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-10T12:52:01.057Z[Etc/UTC]")
public class Verblijfstitel {
  public static final String SERIALIZED_NAME_AANDUIDING = "aanduiding";
  @SerializedName(SERIALIZED_NAME_AANDUIDING)
  private Waardetabel aanduiding;

  public static final String SERIALIZED_NAME_DATUM_EINDE = "datumEinde";
  @SerializedName(SERIALIZED_NAME_DATUM_EINDE)
  private DatumOnvolledig datumEinde;

  public static final String SERIALIZED_NAME_DATUM_INGANG = "datumIngang";
  @SerializedName(SERIALIZED_NAME_DATUM_INGANG)
  private DatumOnvolledig datumIngang;

  public static final String SERIALIZED_NAME_IN_ONDERZOEK = "inOnderzoek";
  @SerializedName(SERIALIZED_NAME_IN_ONDERZOEK)
  private VerblijfstitelInOnderzoek inOnderzoek;


  public Verblijfstitel aanduiding(Waardetabel aanduiding) {
    
    this.aanduiding = aanduiding;
    return this;
  }

   /**
   * Get aanduiding
   * @return aanduiding
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Waardetabel getAanduiding() {
    return aanduiding;
  }


  public void setAanduiding(Waardetabel aanduiding) {
    this.aanduiding = aanduiding;
  }


  public Verblijfstitel datumEinde(DatumOnvolledig datumEinde) {
    
    this.datumEinde = datumEinde;
    return this;
  }

   /**
   * Get datumEinde
   * @return datumEinde
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public DatumOnvolledig getDatumEinde() {
    return datumEinde;
  }


  public void setDatumEinde(DatumOnvolledig datumEinde) {
    this.datumEinde = datumEinde;
  }


  public Verblijfstitel datumIngang(DatumOnvolledig datumIngang) {
    
    this.datumIngang = datumIngang;
    return this;
  }

   /**
   * Get datumIngang
   * @return datumIngang
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public DatumOnvolledig getDatumIngang() {
    return datumIngang;
  }


  public void setDatumIngang(DatumOnvolledig datumIngang) {
    this.datumIngang = datumIngang;
  }


  public Verblijfstitel inOnderzoek(VerblijfstitelInOnderzoek inOnderzoek) {
    
    this.inOnderzoek = inOnderzoek;
    return this;
  }

   /**
   * Get inOnderzoek
   * @return inOnderzoek
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public VerblijfstitelInOnderzoek getInOnderzoek() {
    return inOnderzoek;
  }


  public void setInOnderzoek(VerblijfstitelInOnderzoek inOnderzoek) {
    this.inOnderzoek = inOnderzoek;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Verblijfstitel verblijfstitel = (Verblijfstitel) o;
    return Objects.equals(this.aanduiding, verblijfstitel.aanduiding) &&
        Objects.equals(this.datumEinde, verblijfstitel.datumEinde) &&
        Objects.equals(this.datumIngang, verblijfstitel.datumIngang) &&
        Objects.equals(this.inOnderzoek, verblijfstitel.inOnderzoek);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aanduiding, datumEinde, datumIngang, inOnderzoek);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Verblijfstitel {\n");
    sb.append("    aanduiding: ").append(toIndentedString(aanduiding)).append("\n");
    sb.append("    datumEinde: ").append(toIndentedString(datumEinde)).append("\n");
    sb.append("    datumIngang: ").append(toIndentedString(datumIngang)).append("\n");
    sb.append("    inOnderzoek: ").append(toIndentedString(inOnderzoek)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

