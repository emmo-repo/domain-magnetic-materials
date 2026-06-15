wget --quiet https://github.com/dgarijo/Widoco/releases/download/v1.4.25/widoco-1.4.25-jar-with-dependencies_JDK-17.jar

ontoconvert \
    -sawe \
    --namespace="emmo:https://w3id.org/emmo#" \
    --namespace="magmo:https://w3id.org/emmo/domain/magnetic-materials#" \
    --base-iri="https://w3id.org/emmo/domain/magnetic-materials#" \
    --iri="https://w3id.org/emmo/domain/magnetic-materials" \
    magnetic-materials.ttl \
    "build/magnetic-materials.ttl"

ontoconvert \
    -awe \
    --namespace="emmo:https://w3id.org/emmo#" \
    --namespace="magmo:https://w3id.org/emmo/domain/magnetic-materials#" \
    --base-iri="https://w3id.org/emmo/domain/magnetic-materials#" \
    --iri="https://w3id.org/emmo/domain/magnetic-materials" \
    --copy-annotation="elucidation-->http://purl.org/dc/terms/description" \
    --copy-annotation="prefLabel-->http://www.w3.org/2000/01/rdf-schema#label" \
    magnetic-materials.ttl \
    "build/magnetic-materials-doc.ttl"

keywords \
    -i "build/magnetic-materials-doc.ttl" \
    --write-kw-md "build/magnetic-materials_kw.md" \
    --namespace-filter=https://w3id.org/emmo/domain/magnetic-materials# \
    --redefine=allow

java -jar widoco-1.4.25-jar-with-dependencies_JDK-17.jar \
     -ontFile "build/magnetic-materials-doc.ttl" \
     -outFolder "build/widoco" \
     -getOntologyMetadata \
     -oops \
     -rewriteAll \
     -saveConfig "build/widoco/widoco.conf" \
     -webVowl \
     -licensius \
     -includeAnnotationProperties

ontokit docs --iri-regex=https://w3id.org/emmo/domain/magnetic-materials . && touch public/.nojekyll

cp "build"/*.ttl public/

cp -r "build/widoco" public
