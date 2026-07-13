import pytest

from validatedpatterns_tests.interop import subscription, components, application


@pytest.mark.parametrize(
    "openshift_dyn_client",
    ["HUBCONFIG"],
    indirect=True,
)
def test_subscription_status_hub(openshift_dyn_client):
    expected_subs = { # Sub name: [namsepaces]
        "advanced-cluster-management": ["open-cluster-management"],
        "openshift-gitops-operator": ["openshift-gitops-operator"],
        "openshift-external-secrets-operator": ["external-secrets-operator"],
        "openshift-cert-manager-operator": ["cert-manager-operator"],
        "rhbk-operator": ["keycloak-system"],
        "compliance-operator": ["openshift-compliance"],
        "rhacs-operator": ["openshift-operators"],
        "openshift-zero-trust-workload-identity-manager": ["zero-trust-workload-identity-manager"],
    }

    subscription.assert_subscription_status(
        openshift_dyn_client, expected_subs
    )


@pytest.mark.parametrize(
    "openshift_dyn_client",
    ["HUBCONFIG"],
    indirect=True,
)
def test_site_reachable(openshift_dyn_client):

    components.assert_site_reachable(openshift_dyn_client)


@pytest.mark.parametrize(
    "openshift_dyn_client",
    ["HUBCONFIG"],
    indirect=True,
)
def test_pod_status_hub(openshift_dyn_client):
    projects = [
        "external-secrets-operator",
        "external-secrets",
        "keycloak-system",
        "openshift-compliance",
        "openshift-operators",
        "openshift-gitops",
        "openshift-gitops-operator",
        "open-cluster-management",
        "vault",
        "zero-trust-workload-identity-manager",
        "stackrox",
        "cert-manager",
        "qtodo",
        "vp-gitops",
        "patterns-operator"
    ]

    skip_check = [ "create-auth-provider" ]

    components.assert_pod_status(openshift_dyn_client, projects, skip_check=skip_check)


@pytest.mark.parametrize(
    "openshift_dyn_client",
    ["HUBCONFIG"],
    indirect=True,
)
def test_argocd_reachable(openshift_dyn_client):
    components.assert_argocd_reachable(openshift_dyn_client)


@pytest.mark.parametrize(
    "openshift_dyn_client",
    ["HUBCONFIG"],
    indirect=True,
)
def test_argocd_applications_health(openshift_dyn_client):
    projects = ["openshift-gitops", "layered-zero-trust-hub"]

    application.assert_argocd_applications(
        openshift_dyn_client, projects
    )
