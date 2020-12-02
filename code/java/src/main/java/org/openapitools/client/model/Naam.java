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
import org.openapitools.client.model.NaamInOnderzoek;

/**
 * Naam
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-02T07:33:59.951Z[Etc/UTC]")
public class Naam {
  public static final String SERIALIZED_NAME_GESLACHTSNAAM = "geslachtsnaam";
  @SerializedName(SERIALIZED_NAME_GESLACHTSNAAM)
  private String geslachtsnaam;

  public static final String SERIALIZED_NAME_VOORLETTERS = "voorletters";
  @SerializedName(SERIALIZED_NAME_VOORLETTERS)
  private String voorletters;

  public static final String SERIALIZED_NAME_VOORNAMEN = "voornamen";
  @SerializedName(SERIALIZED_NAME_VOORNAMEN)
  private String voornamen;

  public static final String SERIALIZED_NAME_VOORVOEGSEL = "voorvoegsel";
  @SerializedName(SERIALIZED_NAME_VOORVOEGSEL)
  private String voorvoegsel;

  public static final String SERIALIZED_NAME_IN_ONDERZOEK = "inOnderzoek";
  @SerializedName(SERIALIZED_NAME_IN_ONDERZOEK)
  private NaamInOnderzoek inOnderzoek;


  public Naam geslachtsnaam(String geslachtsnaam) {
    
    this.geslachtsnaam = geslachtsnaam;
    return this;
  }

   /**
   * De achternaam van een persoon. 
   * @return geslachtsnaam
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "Vries", value = "De achternaam van een persoon. ")

  public String getGeslachtsnaam() {
    return geslachtsnaam;
  }


  public void setGeslachtsnaam(String geslachtsnaam) {
    this.geslachtsnaam = geslachtsnaam;
  }


  public Naam voorletters(String voorletters) {
    
    this.voorletters = voorletters;
    return this;
  }

   /**
   * De voorletters van de persoon, afgeleid van de voornamen. 
   * @return voorletters
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "P.J.", value = "De voorletters van de persoon, afgeleid van de voornamen. ")

  public String getVoorletters() {
    return voorletters;
  }


  public void setVoorletters(String voorletters) {
    this.voorletters = voorletters;
  }


  public Naam voornamen(String voornamen) {
    
    this.voornamen = voornamen;
    return this;
  }

   /**
   * De verzameling namen voor de geslachtsnaam, gescheiden door spaties. 
   * @return voornamen
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "Pieter Jan", value = "De verzameling namen voor de geslachtsnaam, gescheiden door spaties. ")

  public String getVoornamen() {
    return voornamen;
  }


  public void setVoornamen(String voornamen) {
    this.voornamen = voornamen;
  }


  public Naam voorvoegsel(String voorvoegsel) {
    
    this.voorvoegsel = voorvoegsel;
    return this;
  }

   /**
   * Get voorvoegsel
   * @return voorvoegsel
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "de", value = "")

  public String getVoorvoegsel() {
    return voorvoegsel;
  }


  public void setVoorvoegsel(String voorvoegsel) {
    this.voorvoegsel = voorvoegsel;
  }


  public Naam inOnderzoek(NaamInOnderzoek inOnderzoek) {
    
    this.inOnderzoek = inOnderzoek;
    return this;
  }

   /**
   * Get inOnderzoek
   * @return inOnderzoek
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public NaamInOnderzoek getInOnderzoek() {
    return inOnderzoek;
  }


  public void setInOnderzoek(NaamInOnderzoek inOnderzoek) {
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
    Naam naam = (Naam) o;
    return Objects.equals(this.geslachtsnaam, naam.geslachtsnaam) &&
        Objects.equals(this.voorletters, naam.voorletters) &&
        Objects.equals(this.voornamen, naam.voornamen) &&
        Objects.equals(this.voorvoegsel, naam.voorvoegsel) &&
        Objects.equals(this.inOnderzoek, naam.inOnderzoek);
  }

  @Override
  public int hashCode() {
    return Objects.hash(geslachtsnaam, voorletters, voornamen, voorvoegsel, inOnderzoek);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Naam {\n");
    sb.append("    geslachtsnaam: ").append(toIndentedString(geslachtsnaam)).append("\n");
    sb.append("    voorletters: ").append(toIndentedString(voorletters)).append("\n");
    sb.append("    voornamen: ").append(toIndentedString(voornamen)).append("\n");
    sb.append("    voorvoegsel: ").append(toIndentedString(voorvoegsel)).append("\n");
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

