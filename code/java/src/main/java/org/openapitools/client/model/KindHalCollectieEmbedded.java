/*
 * Bevragen Ingeschreven Personen
 * API voor het bevragen van ingeschreven personen uit de basisregistratie personen (BRP), inclusief de registratie niet-ingezeten (RNI). Met deze API kun je personen zoeken en actuele gegevens over personen, kinderen, partners en ouders raadplegen.  Gegevens die er niet zijn of niet actueel zijn krijg je niet terug. Heeft een persoon bijvoorbeeld geen geldige nationaliteit, en alleen een beëindigd partnerschap, dan krijg je geen gegevens over nationaliteit en partner.  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/tree/v1.1.0/features) voor nadere toelichting. 
 *
 * The version of the OpenAPI document: 1.3.0
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
import org.openapitools.client.model.KindHalBasis;

/**
 * KindHalCollectieEmbedded
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-03-02T09:47:37.422Z[Etc/UTC]")
public class KindHalCollectieEmbedded {
  public static final String SERIALIZED_NAME_KINDEREN = "kinderen";
  @SerializedName(SERIALIZED_NAME_KINDEREN)
  private List<KindHalBasis> kinderen = null;


  public KindHalCollectieEmbedded kinderen(List<KindHalBasis> kinderen) {
    
    this.kinderen = kinderen;
    return this;
  }

  public KindHalCollectieEmbedded addKinderenItem(KindHalBasis kinderenItem) {
    if (this.kinderen == null) {
      this.kinderen = new ArrayList<>();
    }
    this.kinderen.add(kinderenItem);
    return this;
  }

   /**
   * Get kinderen
   * @return kinderen
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<KindHalBasis> getKinderen() {
    return kinderen;
  }


  public void setKinderen(List<KindHalBasis> kinderen) {
    this.kinderen = kinderen;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    KindHalCollectieEmbedded kindHalCollectieEmbedded = (KindHalCollectieEmbedded) o;
    return Objects.equals(this.kinderen, kindHalCollectieEmbedded.kinderen);
  }

  @Override
  public int hashCode() {
    return Objects.hash(kinderen);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class KindHalCollectieEmbedded {\n");
    sb.append("    kinderen: ").append(toIndentedString(kinderen)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

