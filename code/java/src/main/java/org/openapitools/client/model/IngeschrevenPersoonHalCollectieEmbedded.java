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
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.IngeschrevenPersoonHal;

/**
 * IngeschrevenPersoonHalCollectieEmbedded
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-02T07:33:59.951Z[Etc/UTC]")
public class IngeschrevenPersoonHalCollectieEmbedded {
  public static final String SERIALIZED_NAME_INGESCHREVENPERSONEN = "ingeschrevenpersonen";
  @SerializedName(SERIALIZED_NAME_INGESCHREVENPERSONEN)
  private List<IngeschrevenPersoonHal> ingeschrevenpersonen = null;


  public IngeschrevenPersoonHalCollectieEmbedded ingeschrevenpersonen(List<IngeschrevenPersoonHal> ingeschrevenpersonen) {
    
    this.ingeschrevenpersonen = ingeschrevenpersonen;
    return this;
  }

  public IngeschrevenPersoonHalCollectieEmbedded addIngeschrevenpersonenItem(IngeschrevenPersoonHal ingeschrevenpersonenItem) {
    if (this.ingeschrevenpersonen == null) {
      this.ingeschrevenpersonen = new ArrayList<>();
    }
    this.ingeschrevenpersonen.add(ingeschrevenpersonenItem);
    return this;
  }

   /**
   * Get ingeschrevenpersonen
   * @return ingeschrevenpersonen
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<IngeschrevenPersoonHal> getIngeschrevenpersonen() {
    return ingeschrevenpersonen;
  }


  public void setIngeschrevenpersonen(List<IngeschrevenPersoonHal> ingeschrevenpersonen) {
    this.ingeschrevenpersonen = ingeschrevenpersonen;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IngeschrevenPersoonHalCollectieEmbedded ingeschrevenPersoonHalCollectieEmbedded = (IngeschrevenPersoonHalCollectieEmbedded) o;
    return Objects.equals(this.ingeschrevenpersonen, ingeschrevenPersoonHalCollectieEmbedded.ingeschrevenpersonen);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ingeschrevenpersonen);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IngeschrevenPersoonHalCollectieEmbedded {\n");
    sb.append("    ingeschrevenpersonen: ").append(toIndentedString(ingeschrevenpersonen)).append("\n");
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

