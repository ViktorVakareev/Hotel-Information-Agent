# Test Cases — User Story Scenarios

Each test case below verifies the corresponding user story in `user-stories.md`, using the standard test case template from the course (Test Case Name, Test Purpose, Description, Input, Expected Output, Pass/Fail Criteria, Actual Output, Result). `Actual Output` and `Result` are left blank for you to fill in after running each one in the Playground or Evaluation tab.

---

### TC-01 — Multi-part amenity question (Sara)
**Test Purpose:** Confirm the agent can answer two unrelated amenity questions in one exchange, each grounded in its own source document.
**Description:** A guest asks about pet policy and restaurant hours in a single message.
**Input:** "Are dogs allowed, and what time does the restaurant open for dinner?"
**Expected Output:** A response addressing both questions separately, each with a `[Source: filename]` citation to the correct document (pet policy doc; restaurant hours doc).
**Pass/Fail Criteria:** Pass only if both questions are answered correctly and each is cited to the right source. Fail if either question is skipped, merged incorrectly, or cited to the wrong document.
**Actual Output:**
**Result:**

---

### TC-02 — End-to-end booking request (Marcus)
**Test Purpose:** Confirm the agent can check availability and produce a bookable confirmation from a single, time-pressured request.
**Description:** A guest requests a specific room type for specific dates and expects a fast, complete answer.
**Input:** "Do you have a standard room available for tonight and tomorrow night?"
**Expected Output:** Availability confirmation with room type, price, and either a booking confirmation or clear next steps to complete one — no follow-up questions unless dates/room type were ambiguous.
**Pass/Fail Criteria:** Pass if availability and price are accurate and actionable in one turn. Fail if the agent asks for information already provided, or gives an answer that doesn't match actual availability.
**Actual Output:**
**Result:**

---

### TC-03 — Non-English query with language detection (Elena)
**Test Purpose:** Confirm the agent detects a non-English query and responds in the same language without losing accuracy.
**Description:** A guest asks about spa hours in Spanish.
**Input:** "¿A qué hora abre el spa?"
**Expected Output:** A correct, Spanish-language answer stating the spa's actual hours, with an offer to continue in English if preferred.
**Pass/Fail Criteria:** Pass if the response is in Spanish, factually correct, and grammatically coherent. Fail if the agent responds in English, mistranslates the hours, or produces a nonsensical reply.
**Actual Output:**
**Result:**

---

### TC-04 — Two unrelated requests in one message (James)
**Test Purpose:** Confirm the agent handles a policy question and a service request together without dropping either one.
**Description:** A guest asks about late checkout and requests extra towels in the same message.
**Input:** "Can I get a late checkout, and can someone bring extra towels to room 215?"
**Expected Output:** Confirms the checkout policy and offers to request a late checkout; separately confirms housekeeping will be notified about the towels for room 215.
**Pass/Fail Criteria:** Pass only if both requests are addressed. Fail if only one is handled, or the room number is dropped from the towel request.
**Actual Output:**
**Result:**

---

### TC-05 — Negative sentiment triggers escalation (Aisha)
**Test Purpose:** Confirm the agent detects guest frustration and escalates rather than attempting to self-resolve.
**Description:** A guest reports ongoing noise disruption and expresses frustration about lost sleep.
**Input:** "My room is right next to a construction site and I haven't slept in two nights. This is unacceptable."
**Expected Output:** An empathetic acknowledgment, followed by immediate escalation to hotel management/staff rather than a generic apology-only response or a room-service suggestion.
**Pass/Fail Criteria:** Pass if escalation is triggered and staff contact/handoff is offered. Fail if the agent only apologizes without escalating, or suggests an unrelated fix.
**Actual Output:**
**Result:**

---

### TC-06 — Emergency/urgent query (Tom)
**Test Purpose:** Confirm the agent recognizes a genuine emergency and redirects immediately, per the escalation fix from the earlier testing activity.
**Description:** A guest reports losing his passport shortly before an international flight.
**Input:** "I think I lost my passport and my flight is in 3 hours, what do I do?"
**Expected Output:** Immediate direction to the front desk and the hotel's emergency/security contact — no attempt to guess at passport-replacement procedures itself.
**Pass/Fail Criteria:** Pass if the response is a fast, clear redirect to staff/emergency contact. Fail if the agent gives a vague answer, delays with unrelated questions, or attempts to solve the problem itself.
**Actual Output:**
**Result:**

---

### TC-07 — Same question, different phrasing, on different days (Priya)
**Test Purpose:** Confirm the WiFi knowledge-base fix holds — the same answer is returned regardless of phrasing or session.
**Description:** A guest asks for WiFi details twice, in different words, at different times.
**Input (session 1):** "What's the WiFi password?"
**Input (session 2, next day):** "How do I connect to the internet here?"
**Expected Output:** Identical network name and password returned both times, matching the single consolidated knowledge-base entry.
**Pass/Fail Criteria:** Pass only if both responses match exactly. Fail if the network name or password differs between the two sessions.
**Actual Output:**
**Result:**

---

### TC-08 — Image-based room identification (David)
**Test Purpose:** Confirm the agent's vision integration can identify a room type from an uploaded photo and check its availability.
**Description:** A guest uploads a photo of a room seen on the hotel's website and asks about availability.
**Input:** [Image: photo of a deluxe room] + "Is this room available for June 10–12?"
**Expected Output:** Correct identification of the room type shown in the photo, followed by an accurate availability check for the given dates.
**Pass/Fail Criteria:** Pass if the room type is correctly identified and availability matches actual inventory. Fail if the room type is misidentified or availability is wrong.
**Actual Output:**
**Result:**

---

### TC-09 — Multi-room group request with an out-of-scope question (Chen)
**Test Purpose:** Confirm the agent handles a multi-room request accurately and admits when a question (group discount) is outside its knowledge base.
**Description:** A guest requests multiple rooms for a group and asks about a group discount.
**Input:** "I need 15 standard rooms for March 3–5 for a company offsite. Do you offer a group rate?"
**Expected Output:** Confirms availability/handling for the 15-room request; for the group-rate question, states it doesn't have that information and refers Chen to the sales team rather than inventing a discount figure.
**Pass/Fail Criteria:** Pass if the room request is handled correctly and the discount question gets an honest "I don't know, here's who to ask" answer. Fail if the agent invents a discount percentage or ignores the group-rate question entirely.
**Actual Output:**
**Result:**

---

### TC-10 — Loyalty-program question with an unverifiable guarantee (Robert)
**Test Purpose:** Confirm the agent gives accurate, appropriately hedged information about loyalty benefits rather than over-promising.
**Description:** A returning loyalty member asks about early check-in on arrival day.
**Input:** "I'm a loyalty member — can I get early check-in today?"
**Expected Output:** States what the loyalty program guarantees (if anything) regarding early check-in, and for anything subject to same-day availability, tells Robert to confirm at the front desk rather than promising a guaranteed early check-in.
**Pass/Fail Criteria:** Pass if the response accurately reflects program terms and doesn't guarantee something conditional. Fail if the agent promises early check-in unconditionally or gives incorrect program details.
**Actual Output:**
**Result:**
